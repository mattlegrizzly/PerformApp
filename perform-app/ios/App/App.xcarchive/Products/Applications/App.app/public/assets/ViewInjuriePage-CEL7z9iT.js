import{d as w,V as j,W as b,r as a,o as x,p as k,q as C,c as p,e as _,w as u,f as i,g as t,u as s,t as o,l as I,v as z,k as S,E as V,I as E,h as N}from"./index-BSc-WbhD.js";import{_ as v}from"./NavButton-BzcajF2k.js";import{g as R}from"./perform-body-component-lib-DGzadFkm.js";/* empty css              */import{s as B,a as D}from"./injurie-4Hiekhtv.js";import{u as L}from"./useErrorHandler-eomL11xx.js";import"./index-QnzCfbxr.js";/* empty css                                                  */const T={class:"perform-page"},W={style:{display:"flex","justify-content":"space-between"}},q={style:{color:"black","margin-top":"10px","margin-bottom":"5px"}},P={class:"injuriy_info"},$={class:"injury_item"},H={class:"injury_item"},K={class:"injury_item"},O={style:{display:"flex",width:"100%","margin-top":"40px","justify-content":"center","align-items":"center"}},ee=w({__name:"ViewInjuriePage",setup(A){const{triggerError:f}=L(),r=j(),y=b(),e=a({name:"",description:"",state:"",date:"",zone:[{zone:{name:"",code:""}}]}),c=a(0),g=a("back"),h=a("/list_injuries"),n=a(!1),d=a(Date.now().toString());return x(async()=>{c.value=Number(r.params.id),e.value={id:"",name:"",description:"",zone:[{zone:{name:"",code:""}}],date:"",user:"",state:""},r.query.edit&&(g.value="",h.value+="?edit=true");const l=await k("/injuries/"+c.value+"/",{body:{}},!0);l.status>300?f("Erreur lors de la récupération des blessures"):(e.value=l,n.value=!1,d.value=Date.now().toString(),setTimeout(()=>{n.value=!0},0))}),C(()=>{n.value=!1}),(l,m)=>(p(),_(s(N),{"data-page":"show-injuries"},{default:u(()=>[i(s(E),null,{default:u(()=>[t("div",T,[t("div",W,[i(v,{url:"/list_injuries",text:"Retour",back:""}),i(v,{disabled:e.value.state=="TR",onClick:m[0]||(m[0]=F=>s(y).push("/edit_injurie/"+s(r).params.id)),text:"Editer",noIcon:!0},null,8,["disabled"])]),t("h1",q,o(e.value.name),1),t("p",null,o(e.value.description==""?"Rien à signaler":e.value.description),1),t("div",P,[t("div",$,[t("p",null,o(e.value.zone.name),1)]),t("div",H,[t("p",null,o(new Date(e.value.date).toLocaleString("fr").split(" ")[0]),1)]),t("div",K,[i(s(I),{class:z([s(B)(e.value.state),"injurie_state"])},{default:u(()=>[S(o(s(D)(e.value.state)),1)]),_:1},8,["class"])])]),t("div",O,[n.value?(p(),_(s(R),{key:d.value,muscleSelected:[{zone:e.value.zone}],height:"300",width:"200",viewOnly:"show",isInjury:!0},null,8,["muscleSelected"])):V("",!0)])])]),_:1})]),_:1}))}});export{ee as default};