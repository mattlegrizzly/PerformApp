import{d as T,r,P as $,o as F,s as J,p as M,c as h,e as x,w as s,f as a,g as i,u as l,l as b,v as c,k as v,S as z,U as Z,A as S,B as E,C as q,j as A,J as D,K as N,I as H,h as K,F as W,i as G,D as P,t as R}from"./index-BSc-WbhD.js";import{a as B}from"./index-QnzCfbxr.js";import{_ as O}from"./NavButton-BzcajF2k.js";/* empty css              */import{g as Q}from"./perform-body-component-lib-DGzadFkm.js";import{u as X}from"./useErrorHandler-eomL11xx.js";/* empty css                                                  */const Y={class:"perform-page"},ee={style:{display:"flex","justify-content":"space-between"}},te=i("h1",{style:{color:"black","margin-top":"5px","margin-bottom":"10px"}}," Ajouter une blessure ",-1),le={class:"input_injurie"},ae={class:"input_injurie"},se={class:"input_injurie"},oe={class:"input_injurie"},ne={class:"input_injurie"},ue={style:{display:"flex",width:"100%","margin-top":"16px","justify-content":"center","align-items":"center"}},_e=T({__name:"AddInjuriePage",setup(re){const{triggerError:w}=X(),u=r(!1),n=r(""),j=r(""),y=r(""),p=r(""),d=r([{zone:{name:"",code:""}}]),I=r([]),k=r({}),f=r(!1),U=r([{code:"TR",name:"Soignée"},{code:"NT",name:"Pas soignée"},{code:"IP",name:"En cours"}]);$(n,()=>{n.value.length>0&&(n.value=n.value[0].toUpperCase()+n.value.slice(1))});const m=(o,t)=>{let e=t;switch(o){case"name":e[0]?n.value=e[0].toUpperCase()+e.slice(1):n.value=e;break;case"description":j.value=e;break;case"zone":d.value=[{zone:{code:e,name:""}}];break;case"date":y.value=e;break;case"state":p.value=e;break;case void 0:p.value=""}},V=o=>{const t=I.value.find(e=>e.code==o);d.value=[{zone:{code:t.code,name:t==null?void 0:t.name}}]},C=()=>{const o=document.querySelectorAll("ion-popover");if(o!==null)for(const t of o){const e=t.shadowRoot;if(e===null)return;const _=document.createElement("style");_.textContent=`
      .popover-content {
            margin-left: 9px;
            margin-top: 20px;
      }

    `,e.appendChild(_);const g=document.createElement("style");g.textContent=`
      .sc-ion-select-popover-md-h {
            left : 10px;
            width: calc(100vw - 40px);
      }

    `,t.appendChild(g)}},L=()=>{f.value=!0,W("/injuries/",{body:{name:n.value,description:j.value,zone:d.value[0].zone.code,date:y.value,state:p.value,user:k.value.id}},!0).then(o=>{o.status>300?(w("Erreur lors de la création de la blessure"),u.value=!0,f.value=!1):(u.value=!1,G.push("/view_injuries/"+o.id+"/?edit=true"))})};return F(async()=>{f.value=!1;let o=await J.get("user");o!==""&&(k.value=JSON.parse(o).user);const t=document.querySelectorAll(".custom-ion-select");if(t!==null){for(const e of t){const _=e.shadowRoot;if(_===null)return;const g=document.createElement("style");g.textContent=`
        .select-wrapper-inner {
        width: 100%; /* Ajustez cette valeur selon vos besoins */
        justify-content: space-between;
      }
    `,_.appendChild(g)}M("/workzones/all_injury",{body:{}},!1).then(e=>{e.status>301?w("Erreur lors de la récupération des muscles"):I.value=e})}}),(o,t)=>(h(),x(l(K),{"data-page":"add-injuries"},{default:s(()=>[a(l(H),null,{default:s(()=>[i("div",Y,[i("div",ee,[a(O,{url:"profile",text:"Retour",back:"back"})]),te,i("div",le,[a(l(b),{class:c(u.value&&n.value==""?"required_text":"")},{default:s(()=>[v("Nom de la blessure *")]),_:1},8,["class"]),a(l(z),{"label-placement":"stacked",class:c(u.value&&n.value==""?"required_class":""),fill:"outline",onIonInput:t[0]||(t[0]=e=>m("name",e.detail.value)),placeholder:"Déchirure du quadriceps",value:n.value},null,8,["class","value"])]),i("div",ae,[a(l(b),null,{default:s(()=>[v("Description de la blessure")]),_:1}),a(l(Z),{variant:"outlined",color:"danger",placeholder:"Décrivez votre blessure",onIonChange:t[1]||(t[1]=e=>m("description",e.detail.value))})]),i("div",se,[a(l(b),{class:c(u.value&&d.value[0].zone.code==""?"required_text":"")},{default:s(()=>[v("Zone de la blessure *")]),_:1},8,["class"]),a(l(S),{class:c(["filter-item",u.value&&d.value[0].zone.code==""?"required_class":""])},{default:s(()=>[a(l(E),null,{default:s(()=>[a(l(q),{interface:"popover",placeholder:"Zone de la blessure",class:"custom-ion-select","toggle-icon":l(B),justify:"space-between",onClick:t[2]||(t[2]=e=>C()),onIonChange:t[3]||(t[3]=e=>m("zone",e.detail.value)),value:d.value[0].zone.code},{default:s(()=>[(h(!0),A(N,null,D(I.value,e=>(h(),x(l(P),{key:e.code,value:e.code},{default:s(()=>[v(R(e.name),1)]),_:2},1032,["value"]))),128))]),_:1},8,["toggle-icon","value"])]),_:1})]),_:1},8,["class"])]),i("div",oe,[a(l(b),{class:c(u.value&&y.value==""?"required_text":"")},{default:s(()=>[v("Date de la blessure *")]),_:1},8,["class"]),a(l(z),{class:c(u.value&&y.value==""?"required_class":""),type:"date","label-placement":"stacked",fill:"outline",placeholder:"2021-09-01",onIonChange:t[4]||(t[4]=e=>m("date",e.detail.value))},null,8,["class"])]),i("div",ne,[a(l(b),{class:c(u.value&&p.value==""?"required_text":"")},{default:s(()=>[v("Etat de la blessure *")]),_:1},8,["class"]),a(l(S),{class:c([u.value&&p.value==""?"required_class":"","filter-item"])},{default:s(()=>[a(l(E),null,{default:s(()=>[a(l(q),{interface:"popover",placeholder:"Etat de la blessure",class:"custom-ion-select","toggle-icon":l(B),justify:"space-between",onClick:t[5]||(t[5]=e=>C()),onIonChange:t[6]||(t[6]=e=>m("state",e.detail.value))},{default:s(()=>[(h(!0),A(N,null,D(U.value,e=>(h(),x(l(P),{key:e.code,value:e.code},{default:s(()=>[v(R(e.name),1)]),_:2},1032,["value"]))),128))]),_:1},8,["toggle-icon"])]),_:1})]),_:1},8,["class"])]),i("div",ue,[a(l(Q),{setMuscleSelected:V,muscleSelected:d.value,height:"300",width:"200",viewOnly:"edit",isInjury:!0},null,8,["muscleSelected"])]),i("div",null,[a(O,{style:{width:"100%",height:"40px","margin-top":"20px"},onClick:L,disabled:f.value,text:f.value?"Ajout en cours":"Ajouter la blessure",noIcon:!0},null,8,["disabled","text"])])])]),_:1})]),_:1}))}});export{_e as default};
