import{d as $e,W as qe,r as u,V as Le,P as Pe,o as Ae,s as Ke,p as A,c as i,e as k,w as n,g as d,j as v,t as g,E as te,f as s,k as h,u as t,l as C,S as We,z as ge,B as le,C as ye,J as I,K as S,A as ae,v as He,x as F,I as xe,y as Ue,a0 as we,a1 as be,h as Je,L as x,D as ke,M as re,X as Xe,N as Ge,O as Qe}from"./index-BSc-WbhD.js";import{c as Ye,a as Ze,t as et,b as se,d as Ce}from"./index-QnzCfbxr.js";/* empty css              */import{g as tt}from"./perform-body-component-lib-DGzadFkm.js";import{u as lt}from"./useErrorHandler-eomL11xx.js";import{_ as at}from"./_plugin-vue_export-helper-DlAUqK2U.js";const z=K=>(Ge("data-v-c8a0c0ac"),K=K(),Qe(),K),st={id:"header-wrapper"},nt={class:"perform-page"},ot={key:0},it={key:0,style:{"margin-top":"0px"}},rt={key:1,style:{"margin-top":"0px"}},ct={key:1},ut={key:0,style:{"margin-top":"0px"}},dt={class:"filter-div"},pt={key:2,class:"displayFilter"},vt=z(()=>d("p",null,"Filtres actifs :",-1)),ft={style:{padding:"20px 20px 20px 20px",display:"flex","align-items":"center","justify-content":"space-between","flex-wrap":"wrap",height:"83%",overflow:"scroll"}},_t={style:{width:"100%",display:"flex","align-items":"center","justify-content":"space-between"}},mt={style:{display:"flex","align-items":"center"}},ht={class:"input-div"},gt=z(()=>d("h4",null,"Sports :",-1)),yt=z(()=>d("h6",null,"Sélectionnez les sports à filtrer",-1)),xt={class:"input-div"},wt=z(()=>d("h4",null,"Matériels :",-1)),bt=z(()=>d("h6",null,"Sélectionnez les matériels à filtrer",-1)),kt={class:"input-div",style:{"flex-wrap":"wrap","justify-content":"flex-start"}},Ct=z(()=>d("h4",null,"Muscles :",-1)),It=z(()=>d("h6",null,"Sélectionnez les zones à cibler",-1)),St={style:{display:"flex",width:"100%","margin-top":"16px","justify-content":"space-between","align-items":"center"}},Ft={class:"input-div",style:{position:"fixed","margin-top":"10px","margin-bottom":"10px","justify-content":"space-around",display:"flex"}},zt={key:0,class:"exercice-img"},Et={key:1,class:"exercice-thumbnail"},Mt=["src"],Nt={key:0,class:"exercice-img"},Bt={key:1,class:"exercice-thumbnail"},Tt=["src"],Vt=$e({__name:"ListPage",setup(K){const{triggerError:B}=lt(),ce=qe(),ue=[{id:"orderByNameAsc",value:"Nom (Croissant)"},{id:"orderByNameDesc",value:"Nom (Décroissant)"},{id:"orderByDateAsc",value:"Date (Croissant)"},{id:"orderByDateDesc",value:"Date (Décroissant)"},{id:"default",value:"Par défaut"}],de=u(0),E=u(null),T=u(null),V=u(""),W=u({id:"default",value:"Par défaut"}),H=u([]),U=u([]),J=u([]),w=u([]),M=Le(),X=u([]),_=u([]),j=u([]),b=u([]),D=u(0),O=u(0),ne=u(0),pe=u(0),R=u(1),$=u(1),G=u(null),Q=u(!1),oe=u(!1),ve=()=>_.value.length>0||b.value.length>0||w.value.length>0,Ie=()=>{_.value=[],b.value=[],w.value=[],L()},Se=e=>"http://localhost:8000"+e,Fe=()=>{Q.value=!Q.value};Pe(()=>_.value.length|b.value.length|w.value.length,()=>{setTimeout(()=>{G&&G.value.clientHeight&&G.value.clientHeight>43?oe.value=!0:oe.value=!1},100)});const fe=e=>{let l=!1;return b.value.map(o=>{Number(o.material.id)===e.id&&(l=!0)}),l},q=async e=>{e==="refresh"?(H.value=[],D.value=1,Z("").then(l=>{H.value=l})):(D.value=D.value+1,Z("").then(l=>{for(const o of l)H.value.push(o)}))},_e=async e=>{e==="refresh"?(U.value=[],O.value=1,Z("favorite").then(l=>{U.value=l})):(O.value=O.value+1,Z("favorite").then(l=>{for(const o of l)U.value.push(o)}))},ze=e=>{O.value<$.value&&_e(""),setTimeout(()=>e.target.complete(),500)},Ee=e=>{D.value<R.value&&q(""),setTimeout(()=>e.target.complete(),500)},Me=(e,l)=>e&&l?e.sport.id===l.sport.id:e===l,me=e=>{ce.push("/exercises/"+e)},Ne=()=>{T.value.$el.dismiss()},Be=(e,l)=>{if(l==="add"){if(_.value.filter(function(r){return r.zone.code===e}).length==0){const r=X.value.find(p=>p.code==e);_.value.push({zone:{name:r.name,code:r.code}})}}else{let o=_.value.indexOf(e);_.value.map(r=>{r.zone.code===e&&(o=_.value.indexOf(r)),o!==-1&&_.value.splice(o,1)})}},Y=async(e,l,o,r="add")=>{if(l.filter(function(c){return c.zone?Number(c.zone.code)===e:c.material?Number(c.material.code)===e:c.sport?Number(c.sport.code)===e:Number(c.material.id)===e}).length==0&&r=="add"){const c=o.find(m=>m.id==e);l.push({material:c})}else l.map((c,m)=>{c.zone?c.zone.code==e&&l.splice(m,1):c.material?c.material.id==e&&l.splice(m,1):c.sport&&c.sport.id==e&&l.splice(m,1)})},Te=e=>{let l=!1;ue.map(o=>{o.id===e.detail.value&&(W.value=o,l=!0)}),l||(W.value={id:"default",value:"Par défaut"}),setTimeout(()=>{q("refresh")},500)},ie=(e,l="")=>{let o="";for(let r=0;r<e.length;r++)l=="sport"?o+=String(e[r].sport.id):l=="muscle"?o+=String(e[r].zone.code):l=="material"&&(o+=e[r].material.id),r<e.length-1&&(o+=",");return o},L=()=>{const e={};b.value.length>0?e.material_id=ie(b.value,"material"):e.material_id="",_.value.length>0?e.workzone_code=ie(_.value,"muscle"):e.workzone_code="",w.value.length>0?e.sport_id=ie(w.value,"sport"):e.sport_id="",ce.replace({path:M.path,query:Object.assign({},M.query,e)}).then(()=>{q("refresh"),T.value&&T.value.$el.dismiss()})},Z=async e=>{R.value=R.value||1,$.value=$.value||1;const l=e==="favorite",o=l?O.value:D.value,r=l?$.value:R.value;if(o>r)return{};const p={};W.value&&(p.orderBy=W.value),V.value&&(p.search=V.value);const{workzone_code:c,material_id:m,sport_id:y}=M.query;if(m&&(p.material_id=String(m)),y&&(p.sport_id=String(y)),c&&(p.workzone_code=String(c)),l){const f=await A(`/userfavexercises/user/${de.value}/`,p);f.status!==void 0&&f.status>301&&B("Erreur lors de la récupération des exercices favoris");const P=f.map(ee=>ee.fav_exercise);return pe.value=P.length,$.value=Math.ceil(P.length/10),P}else{const f=await A(`/exercises/?page=${o}`,p);return f.status>301&&B("Erreur lors de la récupération des exercices"),ne.value=f.count,R.value=Math.ceil(f.count/10),f.results}},he=()=>{const e=M.query.workzone_code,l=e?e.split(","):[];_.value=l.map(m=>{const y=X.value.find(f=>f.code==m);return{zone:{name:y.name,code:y.code}}});const o=M.query.material_id,r=o?o.split(","):[];b.value=r.map(m=>{const y=j.value.find(f=>f.id==m);return{material:{id:y.id,pictures:"",name:y.name}}});const p=M.query.sport_id,c=p?p.split(","):[];w.value=c.map(m=>{const y=J.value.find(f=>f.id==m);return{sport:{name:y.name,id:Number(y.id)}}})},Ve=()=>{he(),setTimeout(()=>{const e=document.querySelectorAll(".custom-ion-select");if(e!==null)for(const l of e){const o=l.shadowRoot;if(o===null)return;const r=document.createElement("style");r.textContent=`
          .select-wrapper-inner {
          width: 100%; /* Ajustez cette valeur selon vos besoins */
          justify-content: space-between;
        }
      `,o.appendChild(r)}},100),T.value.$el.present()},je=e=>{w.value=e.detail.value},De=async e=>{V.value=e.target.value,q("refresh")};return Ae(async()=>{_.value=[],Ke.get("user").then(e=>{de.value=JSON.parse(e).user.id,_e("refresh")}),q("refresh"),A("/sports/all",{body:{}},!1).then(e=>{e.status>300?B("Erreur lors de la récupération des sports"):(J.value=e,A("/materials/all",{body:{}},!1).then(l=>{l.status>300?B("Erreur lors de la récupération des matériels"):(j.value=l,A("/workzones/all",{body:{}},!1).then(o=>{o.status>300?B("Erreur lors de la récupération des muscles"):(X.value=o,he())}))}))})}),(e,l)=>{const o=x("v-icon"),r=x("v-img"),p=x("v-card-title"),c=x("v-card"),m=x("v-col"),y=x("v-row"),f=x("v-tab"),P=x("v-tabs"),ee=x("v-tabs-window-item"),Oe=x("v-tabs-window"),Re=x("v-card-text");return i(),k(t(Je),{"data-page":"Exercises"},{default:n(()=>[d("div",st,[d("div",nt,[V.value===""?(i(),v("div",ot,[E.value=="one"?(i(),v("h1",it," Exercices ("+g(ne.value)+") ",1)):(i(),v("h1",rt," Exercices favoris ("+g(pe.value)+") ",1))])):(i(),v("div",ct,[E.value=="one"?(i(),v("h1",ut," Résultats de la recherche pour : "+g(V.value)+" ("+g(ne.value)+") ",1)):te("",!0)])),s(t(C),null,{default:n(()=>[h("Rechercher un exercice :")]),_:1}),s(t(We),{id:"search-input",fill:"outline",slot:"end",placeholder:"Cherchez un exercice",shape:"round",onIonInput:l[0]||(l[0]=a=>De(a))}),d("div",dt,[s(t(ge),{onClick:Ve},{default:n(()=>[h("Filtres")]),_:1}),s(t(ae),{class:"filter-item"},{default:n(()=>[s(t(le),null,{default:n(()=>[s(t(ye),{"aria-label":"Trier par",interface:"popover",placeholder:"Trier par",onIonChange:l[1]||(l[1]=a=>Te(a))},{default:n(()=>[(i(),v(S,null,I(ue,a=>s(t(ke),{key:a.id,value:a.id},{default:n(()=>[h(g(a.value),1)]),_:2},1032,["value"])),64))]),_:1})]),_:1})]),_:1})]),ve()?(i(),v("div",pt,[vt,d("div",{class:He(["displayFilterContainer",Q.value?"showFullDisplayContainer":""])},[d("div",{class:"displayFilterChipContainer",ref_key:"chipFilterContainer",ref:G},[(i(!0),v(S,null,I(_.value,a=>(i(),k(t(re),{class:"filter-ion-chip",color:"primary"},{default:n(()=>[s(t(F),{icon:t(se),onClick:()=>{Y(a.zone.code,_.value,X.value,"remove").then(()=>{L()})}},null,8,["icon","onClick"]),s(t(C),null,{default:n(()=>[h(g(a.zone.name),1)]),_:2},1024)]),_:2},1024))),256)),(i(!0),v(S,null,I(w.value,a=>(i(),k(t(re),{key:a.sport.id,class:"filter-ion-chip",color:"primary"},{default:n(()=>[s(t(F),{icon:t(se),onClick:N=>{N.stopPropagation(),Y(a.sport.id,w.value,J.value,"remove"),L()}},null,8,["icon","onClick"]),s(t(C),null,{default:n(()=>[h(g(a.sport.name),1)]),_:2},1024)]),_:2},1024))),128)),(i(!0),v(S,null,I(b.value,a=>(i(),k(t(re),{key:a.material.id,class:"filter-ion-chip",color:"primary"},{default:n(()=>[s(t(F),{icon:t(se),onClick:N=>{N.stopPropagation(),Y(a.material.id,b.value,j.value,"remove"),L()}},null,8,["icon","onClick"]),s(t(C),null,{default:n(()=>[h(g(a.material.name),1)]),_:2},1024)]),_:2},1024))),128))],512),oe.value?(i(),k(t(F),{key:0,onClick:Fe,icon:Q.value?t(Ye):t(Ze)},null,8,["icon"])):te("",!0)],2)])):te("",!0)]),s(t(Ue),{class:"static-modal",ref_key:"filterModal",ref:T},{default:n(()=>[s(t(xe),null,{default:n(()=>[d("div",ft,[d("div",_t,[d("h3",mt,[h(" FILTRER "),ve()?(i(),k(t(F),{key:0,style:{"margin-left":"10px"},onClick:Ie,icon:t(et)},null,8,["icon"])):te("",!0)]),s(t(F),{style:{color:"red",border:"1px solid red","border-radius":"5px"},onClick:Ne,icon:t(se)},null,8,["icon"])]),d("div",ht,[gt,yt,s(t(ae),null,{default:n(()=>[s(t(le),null,{default:n(()=>[s(t(ye),{onIonChange:je,class:"custom-ion-select",value:w.value,"aria-label":"Sports",placeholder:"Selectionner vos sports",multiple:!0,compareWith:Me},{default:n(()=>[(i(!0),v(S,null,I(J.value,a=>(i(),k(t(ke),{value:{sport:{id:a.id,name:a.name}},key:a.id,"aria-selected":"true"},{default:n(()=>[h(g(a.name),1)]),_:2},1032,["value"]))),128))]),_:1},8,["value"])]),_:1})]),_:1})]),d("div",xt,[wt,bt,s(y,{style:{display:"flex","flex-wrap":"wrap","justify-content":"center"},dense:""},{default:n(()=>[(i(!0),v(S,null,I(j.value,a=>(i(),k(m,{style:{width:"30%",flex:"none"},key:a.id,cols:"12",sm:"4"},{default:n(()=>[s(c,{onClick:N=>Y(a.id,b.value,j.value),style:Xe(fe(a)?"box-shadow:inset 0px 0px 0px 2px var(--primary-blue)":"")},{default:n(()=>[s(r,{src:a.pictures?a.pictures.replace("http","https"):"",class:"align-end",gradient:`to bottom, rgba(0,0,0,.05), rgba(0,0,0,.1)
                      `,height:"80px",cover:"","aspect-ratio":"1"},{default:n(()=>[s(o,{icon:fe(a)?"mdi-check":""},null,8,["icon"])]),_:2},1032,["src"]),s(p,{style:{"font-size":"12px",height:"40px",display:"flex","justify-content":"center","align-items":"center","white-space":"normal !important",padding:"5px","text-align":"center"},class:"textTitleCard"},{default:n(()=>[h(g(a.name),1)]),_:2},1024)]),_:2},1032,["onClick","style"])]),_:2},1024))),128))]),_:1})]),d("div",kt,[Ct,It,d("div",St,[s(t(tt),{height:"300",width:"300",viewOnly:"edit",muscleSelected:_.value,setMuscleSelected:Be},null,8,["muscleSelected"])])])]),d("div",Ft,[s(t(ge),{onClick:L},{default:n(()=>[h(" Filtrer ")]),_:1})])]),_:1})]),_:1},512),s(P,{id:"tabs-exercise",modelValue:E.value,"onUpdate:modelValue":l[2]||(l[2]=a=>E.value=a)},{default:n(()=>[s(f,{value:"one"},{default:n(()=>[h("Tous les exercices")]),_:1}),s(f,{value:"two"},{default:n(()=>[h("Mes favoris")]),_:1})]),_:1},8,["modelValue"])]),s(t(xe),{color:"light"},{default:n(()=>[s(Re,null,{default:n(()=>[s(Oe,{modelValue:E.value,"onUpdate:modelValue":l[3]||(l[3]=a=>E.value=a)},{default:n(()=>[s(ee,{value:"one"},{default:n(()=>[s(t(ae),{lines:"none",class:"parent-list",inset:!0},{default:n(()=>[(i(!0),v(S,null,I(H.value,a=>(i(),k(t(le),{class:"list-item",key:a.id,onClick:N=>me(a.id)},{default:n(()=>[a.thumbnail==null?(i(),v("div",zt,[s(t(C),null,{default:n(()=>[h(g(a.name[0]),1)]),_:2},1024)])):(i(),v("div",Et,[d("img",{src:a.thumbnail.replace("http","https"),alt:"Miniature de l'exercice"},null,8,Mt)])),s(t(C),{class:"exercice_label"},{default:n(()=>[h(g(a.name),1)]),_:2},1024),s(t(F),{icon:t(Ce)},null,8,["icon"])]),_:2},1032,["onClick"]))),128))]),_:1}),s(t(we),{onIonInfinite:Ee},{default:n(()=>[s(t(be))]),_:1})]),_:1}),s(ee,{value:"two"},{default:n(()=>[s(t(ae),{lines:"none",class:"parent-list",inset:!0},{default:n(()=>[(i(!0),v(S,null,I(U.value,a=>(i(),k(t(le),{class:"list-item",key:a.id,onClick:N=>me(a.id)},{default:n(()=>[a.thumbnail==null?(i(),v("div",Nt,[s(t(C),null,{default:n(()=>[h(g(a.name[0]),1)]),_:2},1024)])):(i(),v("div",Bt,[d("img",{src:Se(a.thumbnail),alt:"Miniature de l'exercice"},null,8,Tt)])),s(t(C),{class:"exercice_label"},{default:n(()=>[h(g(a.name),1)]),_:2},1024),s(t(F),{icon:t(Ce)},null,8,["icon"])]),_:2},1032,["onClick"]))),128))]),_:1}),s(t(we),{onIonInfinite:ze},{default:n(()=>[s(t(be))]),_:1})]),_:1})]),_:1},8,["modelValue"])]),_:1})]),_:1})]),_:1})}}}),Lt=at(Vt,[["__scopeId","data-v-c8a0c0ac"]]);export{Lt as default};