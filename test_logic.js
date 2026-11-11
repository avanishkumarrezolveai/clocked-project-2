const fs=require('fs'),vm=require('vm'),path=require('path');
const root=__dirname;
const els={};
function el(id){return els[id]??(els[id]={id,innerHTML:'',textContent:'',value:'',classList:{add(){},remove(){},toggle(){}},addEventListener(){},setAttribute(){},removeAttribute(){}})}
const d={getElementById:el,querySelectorAll:()=>[]};
const loc={getItem(){return null},setItem(){},removeItem(){}};
const ctx=vm.createContext({window:{},document:d,localStorage:loc,console,setTimeout,clearTimeout,Date,Blob,URL});
vm.runInContext(fs.readFileSync(path.join(root,'data.js'),'utf8'),ctx);
vm.runInContext(fs.readFileSync(path.join(root,'app.js'),'utf8'),ctx);
function check(expr,msg){if(!vm.runInContext(expr,ctx))throw Error(msg); console.log('PASS',msg)}
check('DB.users.length===200 && DB.assets.length===200','Shared datasets loaded');
check('DB.service_offers.length===200 && DB.incident_offers.length===15','Offerings loaded');
check('DB.mappings.length===430 && DB.demo_cases.length===46','Mappings and test cases loaded');
check('state.page==="overview" && !!document.getElementById("main").innerHTML','Overview renders');
vm.runInContext('state.decision=evaluate(state.utterance,getCase());state.page="studio";state.step=2;render();',ctx);
check('state.decision.selected.offering_id==="INC001"','Expected T003 incident selected');
check('state.decision.needsAsset && state.decision.assets.length===3','Three matching Dell devices require clarification');
check('state.decision.related.some(x=>x.ticket.channel==="Service Portal")','Cross channel ticket match');
check('document.getElementById("main").innerHTML.includes("Latitude 5440")','Validation view displays owned assets');
vm.runInContext('state.page="tickets";render();state.page="agent";render()',ctx);
check('document.getElementById("main").innerHTML.includes("Configuration overlap audit")','Agent Studio audit renders');
vm.runInContext('state.page="assets";render();state.page="users";render();state.page="knowledge";render();state.page="livechat";render();state.page="framework";render();state.page="feedback";render();',ctx);
check('state.page==="feedback"','All connected module views render');
console.log('ALL LOGIC TESTS PASS');
