import{d as C,V as E,W,r as i,o as $,s as P,c as R,e as M,w as a,f as e,g as o,t as c,u as s,l as p,k as n,z as _,y as N,I as V,h as j,T as B,p as F,N as J,O as z}from"./index-BSc-WbhD.js";import{_ as h}from"./NavButton-BzcajF2k.js";/* empty css              */import{u as L}from"./useErrorHandler-eomL11xx.js";import{J as v}from"./Jauge-vMOM0fAB.js";import{_ as O}from"./_plugin-vue_export-helper-DlAUqK2U.js";import"./index-QnzCfbxr.js";/* empty css                                                  */const T=d=>(J("data-v-7d18950c"),d=d(),z(),d),q={class:"perform-page"},A={style:{display:"flex","justify-content":"space-between"}},H={style:{color:"black","margin-top":"5px","margin-bottom":"10px"}},Y={style:{display:"flex","flex-wrap":"wrap"}},G={style:{display:"flex","justify-content":"space-between"}},K={style:{width:"40%"}},Q={style:{width:"40%"}},U={style:{position:"absolute",bottom:"10px",width:"calc(100% - var(--pd-r) - var(--pd-l))",display:"flex","justify-content":"center"}},X=T(()=>o("div",null,[o("h4",{style:{"font-size":"15px",padding:"0px 20px"}},"Supprimer cet séance ?")],-1)),Z={style:{position:"absolute",bottom:"10px",width:"calc(100%)",display:"flex","justify-content":"space-around"}},ee=C({__name:"ShowWorkoutPage",setup(d){const{triggerError:f}=L(),m=E(),y=W(),u=i(null),g=i(5),w=i(5),k=i({user:{id:0}}),x=i(""),r=i({id:0,name:"",date:x.value,workout_description:"",cognitive_rpe:g.value,physical_rpe:w.value,time_value:"",user:0}),S=()=>{const t=new Date(r.value.date),l=t.getFullYear(),D=String(t.getMonth()+1).padStart(2,"0");return`${String(t.getDate()).padStart(2,"0")}-${D}-${l}`},I=()=>{B("/workout/"+m.params.id,!0).then(t=>{t.status&&t.status>300?f("Erreur à la suppression de l'entrainement"):(y.push("/coaching"),u.value.$el.dismiss())})},b=()=>{F("/workout/"+m.params.id,{body:{}},!0).then(t=>{t.status>300?f("Erreur à la récupération de l'entrainement"):r.value=t})};return $(async()=>{const t=await P.get("user");k.value=JSON.parse(t),b()}),(t,l)=>(R(),M(s(j),{"data-page":"ShowWorkout"},{default:a(()=>[e(s(V),null,{default:a(()=>[o("div",q,[o("div",A,[e(h,{url:"/coaching",text:"Retour"}),e(h,{url:"/workout_edit/"+r.value.id,text:"Modifier",noIcon:!0},null,8,["url"])]),o("h1",H,c(r.value.name),1),o("h5",null,c(S()),1),o("div",Y,[e(s(p),{position:"stacked",style:{width:"100%"}},{default:a(()=>[n(c(r.value.time_value),1)]),_:1}),e(s(p),{position:"stacked",style:{width:"100%"}},{default:a(()=>[n(c(r.value.workout_description),1)]),_:1})]),o("div",G,[o("div",K,[e(s(p),{position:"stacked"},{default:a(()=>[n("RPE Cognitif")]),_:1}),e(v,{value:r.value.cognitive_rpe},null,8,["value"])]),o("div",Q,[e(s(p),{position:"stacked"},{default:a(()=>[n("RPE Physique")]),_:1}),e(v,{value:r.value.physical_rpe},null,8,["value"])])]),o("div",U,[e(s(_),{onClick:l[0]||(l[0]=()=>u.value.$el.present()),color:"danger",style:{width:"100%"}},{default:a(()=>[n(" Supprimer ")]),_:1}),e(s(N),{ref_key:"deleteModal",ref:u,id:"info_wellness_modal"},{default:a(()=>[X,o("div",Z,[e(s(_),{onClick:l[1]||(l[1]=()=>u.value.$el.dismiss()),color:"",style:{width:"40%"}},{default:a(()=>[n(" Annuler ")]),_:1}),e(s(_),{onClick:I,color:"danger",style:{width:"40%"}},{default:a(()=>[n(" Supprimer ")]),_:1})])]),_:1},512)])])]),_:1})]),_:1}))}}),ce=O(ee,[["__scopeId","data-v-7d18950c"]]);export{ce as default};
