import{d as H,V as z,W as J,r as u,n as O,o as Y,s as K,c as w,e as G,w as d,f as o,g as l,k as i,t as C,u as n,l as p,v as c,S as h,U as Q,j as q,J as P,K as R,m as A,I as X,h as Z,F as ee,N as ae,O as te}from"./index-BSc-WbhD.js";import{_ as E}from"./NavButton-BzcajF2k.js";/* empty css              */import{u as le}from"./useErrorHandler-eomL11xx.js";import{_ as se}from"./_plugin-vue_export-helper-DlAUqK2U.js";import"./index-QnzCfbxr.js";/* empty css                                                  */const oe=k=>(ae("data-v-64d0c63a"),k=k(),te(),k),ne={class:"perform-page"},ue={style:{display:"flex","justify-content":"space-between"}},ie={style:{color:"black","margin-top":"5px","margin-bottom":"10px"}},re=oe(()=>l("br",null,null,-1)),de={class:"input_injurie"},ce={class:"input_injurie"},pe={class:"input_injurie"},ve={class:"time-input"},me={class:"input_injurie"},_e={class:"range-labels"},ge={class:"range_inner"},fe={class:"input_injurie"},he={class:"range-labels"},ke={class:"range_inner"},be=H({__name:"AddWorkoutPage",setup(k){const{triggerError:U}=le(),L=z(),N=J(),v=u(5),m=u(5),r=u(!1),_=u(""),g=u(""),f=u(""),$=u({user:{id:0}}),b=u(""),t=u({name:"",date:b.value,workout_description:"",cognitive_rpe:v.value,physical_rpe:m.value,time_value:"",user:0}),y=u(!1),W=s=>{const[a,e,V]=s.split(":").map(I=>I.padStart(2,"0"));return`00 ${a}:${e}:${V}`},F=O(()=>`${_.value}:${g.value}:${f.value}`),M=()=>{y.value=!0,t.value.user=$.value.user.id,t.value.date=new Date(b.value);const s=W(F.value);t.value.time_value=s,ee("/workout/",{body:t.value},!0).then(a=>{a.status>300?U(a.data):N.push("/coaching")})},x=()=>_.value!==""||g.value!=""||f.value!="",j=s=>{s.target.id==="cognitive"?(v.value=s.detail.value,t.value.cognitive_rpe=s.detail.value):(m.value=s.detail.value,t.value.physical_rpe=s.detail.value)},D=(s,a)=>{let e=a;switch(s){case"name":e[0]?t.value.name=e[0].toUpperCase()+e.slice(1):t.value.name=e;break;case"description":t.value.workout_description=e;break;case"date":b.value=e;break;case"cogntive":t.value.cognitive_rpe=e;break;case"physical":t.value.physical_rpe=e;break;case"time":t.value.time_value=e;break}},T=()=>{const s=new Date(t.value.date),a=s.getFullYear(),e=String(s.getMonth()+1).padStart(2,"0");return`${String(s.getDate()).padStart(2,"0")}-${e}-${a}`};return Y(async()=>{t.value.name="",t.value.workout_description="",v.value=5,m.value=5,_.value="",g.value="",f.value="";const s=L.params.date,a=new Date(s),e=a.getFullYear(),V=String(a.getMonth()+1).padStart(2,"0"),S=String(a.getDate()).padStart(2,"0"),I=`${e}-${V}-${S}`;t.value.date=I,b.value=I;const B=await K.get("user");$.value=JSON.parse(B),y.value=!1}),(s,a)=>(w(),G(n(Z),{"data-page":"AddWorkout"},{default:d(()=>[o(n(X),null,{default:d(()=>[l("div",ne,[l("div",ue,[o(E,{url:"profile",text:"Retour",back:"back"})]),l("h1",ie,[i(" Créer votre séance pour le "),re,i(C(T()),1)]),l("div",de,[o(n(p),{position:"stacked",class:c(r.value&&t.value.name==""?"required_text":"")},{default:d(()=>[i("Nom de la séance")]),_:1},8,["class"]),o(n(h),{class:c(r.value&&t.value.name==""?"required_class":""),type:"text","label-placement":"stacked",fill:"outline",placeholder:"Séance VMA",onIonChange:a[0]||(a[0]=e=>D("name",e.detail.value))},null,8,["class"])]),l("div",ce,[o(n(p),{position:"stacked"},{default:d(()=>[i("Description de la séance")]),_:1}),o(n(Q),{variant:"outlined",placeholder:"Décrivez votre séance",onIonChange:a[1]||(a[1]=e=>D("description",e.detail.value)),rows:4})]),l("div",pe,[o(n(p),{position:"stacked",class:c(r.value&&t.value.date==""?"required_text":"")},{default:d(()=>[i("Date")]),_:1},8,["class"]),o(n(h),{class:c(r.value&&t.value.date==""?"required_class":""),type:"date",value:t.value.date,"label-placement":"stacked",fill:"outline",placeholder:"12/03/2023",onIonChange:a[2]||(a[2]=e=>D("date",e.detail.value))},null,8,["class","value"])]),l("div",null,[o(n(p),{position:"stacked",class:c(r.value&&!x()?"required_text":"")},{default:d(()=>[i("Temps (en hh:mm:ss)")]),_:1},8,["class"]),l("div",ve,[o(n(h),{modelValue:_.value,"onUpdate:modelValue":a[3]||(a[3]=e=>_.value=e),"aria-label":"hours",type:"number",labelPlacement:void 0,placeholder:"HH",maxLength:"2",class:c(["time_input",r.value&&!x()?"required_class":""]),style:{"padding-inline-start":"0px","--padding-end":"0px"}},null,8,["modelValue","class"]),i(": "),o(n(h),{modelValue:g.value,"onUpdate:modelValue":a[4]||(a[4]=e=>g.value=e),type:"number",placeholder:"MM","aria-label":"minutes",labelPlacement:void 0,maxLength:"2",class:c(["time_input",r.value&&!x()?"required_class":""])},null,8,["modelValue","class"]),i(": "),o(n(h),{modelValue:f.value,"onUpdate:modelValue":a[5]||(a[5]=e=>f.value=e),type:"number",placeholder:"SS","aria-label":"secondes",labelPlacement:void 0,maxLength:"2",class:c(["time_input",r.value&&!x()?"required_class":""])},null,8,["modelValue","class"])])]),l("div",null,[l("div",me,[o(n(p),{position:"stacked"},{default:d(()=>[i("RPE Cognitif")]),_:1}),l("div",_e,[(w(),q(R,null,P(10,e=>l("div",{key:e,class:"range-label"},C(e),1)),64))]),l("div",ge,[o(n(A),{modelValue:v.value,"onUpdate:modelValue":a[6]||(a[6]=e=>v.value=e),"aria-label":"Difficulté",ticks:!0,snaps:!0,min:1,max:10,class:"difficulty-slider",onIonChange:j,id:"cognitive"},null,8,["modelValue"])])]),l("div",fe,[o(n(p),{position:"stacked"},{default:d(()=>[i("RPE Physique")]),_:1}),l("div",he,[(w(),q(R,null,P(10,e=>l("div",{key:e,class:"range-label"},C(e),1)),64))]),l("div",ke,[o(n(A),{modelValue:m.value,"onUpdate:modelValue":a[7]||(a[7]=e=>m.value=e),"aria-label":"Difficulté",id:"phsyical",ticks:!0,snaps:!0,min:1,max:10,onIonChange:j,class:"difficulty-slider"},null,8,["modelValue"])])])]),l("div",null,[o(E,{style:{width:"100%",height:"40px","margin-top":"20px"},onClick:M,disabled:y.value,text:y.value?"Ajout en cours":"Ajouter la séance",noIcon:!0},null,8,["disabled","text"])])])]),_:1})]),_:1}))}}),Ce=se(be,[["__scopeId","data-v-64d0c63a"]]);export{Ce as default};