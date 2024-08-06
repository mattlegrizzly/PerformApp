import{d as w,c as i,e as p,w as s,g as e,f as a,u as o,ab as v,ac as A,ad as G,k as m,t as n,M as b,ae as q,N as D,O as H,j as f,K as M,J as B,r as u,I as C,h as I}from"./index-BSc-WbhD.js";import{a as V,S as j}from"./swiper-vue-DyqhViDQ.js";import{_ as x}from"./_plugin-vue_export-helper-DlAUqK2U.js";const S=r=>(D("data-v-a7157d8f"),r=r(),H(),r),P={class:"img_div"},Y=["src"],W={class:"description-text"},F={style:{"font-weight":"600",width:"100%","font-size":"8px"}},U={style:{display:"flex","justify-content":"space-between"}},$={style:{"font-weight":"600"}},N=S(()=>e("p",null,"Voir plus",-1)),k=w({__name:"SquareProgam",props:["program"],setup(r){const t=r;return(l,d)=>(i(),p(o(q),null,{default:s(()=>[e("div",P,[e("img",{class:"img_program",alt:"Silhouette of mountains",src:t.program.photo_url},null,8,Y)]),a(o(v)),a(o(A),{class:"description_card_program"},{default:s(()=>[a(o(G),{class:"program-title"},{default:s(()=>[m(n(t.program.title),1)]),_:1}),a(o(b),null,{default:s(()=>[m(n(t.program.sport),1)]),_:1}),e("p",W,n(t.program.description),1),e("p",F,"Durée "+n(t.program.duration),1),e("div",U,[e("p",$,n(t.program.price),1),N])]),_:1})]),_:1}))}}),T=x(k,[["__scopeId","data-v-a7157d8f"]]),R={class:"sport-programs"},E={__name:"SliderComponents",props:["programs"],setup(r){const t=r;return(l,d)=>(i(),f("div",R,[a(o(j),{style:{padding:"20px 10px 20px 10px"},"slides-per-view":2.2,"space-between":5,pagination:""},{default:s(()=>[(i(!0),f(M,null,B(t.programs,(g,h)=>(i(),p(o(V),{key:h},{default:s(()=>[a(T,{program:g},null,8,["program"])]),_:2},1024))),128))]),_:1})]))}},_=x(E,[["__scopeId","data-v-4d4ef035"]]),c=r=>(D("data-v-315c2cdf"),r=r(),H(),r),L=c(()=>e("div",{class:"perform-page"},[e("h1",{style:{color:"black","margin-top":"5px","margin-bottom":"10px"}}," Nos programmes ")],-1)),z={class:"program_page"},J=c(()=>e("h2",null,"Catégories",-1)),K={class:"sports_chip"},O=c(()=>e("h2",null,"Nos meilleurs programmes",-1)),Q=c(()=>e("div",{class:"program_page"},[e("h2",null,"Les programmes recommandés pour vous")],-1)),X=w({__name:"ProgramsPage",setup(r){const t=u(["CrossFit","Pilate","Fitness","Boxe"]),l=u([{title:"Bootcamp Énergie",sport:"Renforcement",description:"Un programme intense qui combine des exercices de cardio, de renforcement musculaire et de haute intensité. Idéal pour ceux qui cherchent à repousser leurs limites.",duration:"4 semaines",price:"120€",photo_url:"https://images.unsplash.com/photo-1534258936925-c58bed479fcb?q=80&w=1931&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},{title:"Yoga Relaxation",sport:"Yoga",description:"Un programme de yoga conçu pour améliorer la flexibilité, réduire le stress et renforcer la connexion corps-esprit. Parfait pour débutants et intermédiaires.",duration:"6 semaines",price:"90€",photo_url:"https://images.unsplash.com/photo-1560233075-4c1e2007908e?q=80&w=1915&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},{title:"Fit & Sculpt",sport:"Fitness",description:"Ce programme combine des exercices de musculation et de cardio pour sculpter le corps, tonifier les muscles et améliorer l'endurance.",duration:"8 semaines",price:"150€",photo_url:"https://images.unsplash.com/photo-1627483298606-cf54c61779a9?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},{title:"CrossFit Challenge",sport:"CrossFit",description:"Un programme de CrossFit pour développer force, agilité et endurance. Idéal pour ceux qui aiment les défis et les entraînements variés.",duration:"5 semaines",price:"130€",photo_url:"https://images.unsplash.com/photo-1536922246289-88c42f957773?q=80&w=2104&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},{title:"Pilates Reforme",sport:"Pilate",description:"Un programme de Pilates utilisant des appareils pour un entraînement ciblé et efficace, parfait pour renforcer les muscles profonds et améliorer la posture.",duration:"7 semaines",price:"110€",photo_url:"https://images.unsplash.com/photo-1717500251646-3e661a2ee7e1?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},{title:"Cardio Boxing",sport:"Boxe",description:"Un programme de cardio boxing qui mélange techniques de boxe et exercices cardiovasculaires pour brûler des calories et améliorer la coordination.",duration:"6 semaines",price:"100€",photo_url:"https://images.unsplash.com/photo-1606045486656-13a37890dc90?q=80&w=1984&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"}]),d=u([{titre:"Circuit Training Dynamique",description:"Un programme combinant des exercices de haute intensité et de renforcement musculaire, parfait pour brûler des calories rapidement.",durée:"4 semaines",prix:"130€",photo_url:"https://images.unsplash.com/photo-1516481265257-97e5f4bc50d5?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",sport:"Circuit Training"},{titre:"Running Endurance",description:"Un programme de course à pied conçu pour améliorer l'endurance et la vitesse, idéal pour les amateurs de running.",durée:"6 semaines",prix:"100€",photo_url:"https://images.unsplash.com/photo-1596460456678-760115935178?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",sport:"Running"},{titre:"HIIT Fat Burner",description:"Un programme d'entraînement par intervalles de haute intensité pour brûler des graisses et améliorer la condition physique.",durée:"4 semaines",prix:"140€",photo_url:"https://images.unsplash.com/photo-1500468756762-a401b6f17b46?q=80&w=1888&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",sport:"HIIT"},{titre:"Cyclisme de Montagne",description:"Un programme d'entraînement intensif pour les passionnés de vélo, ciblant la force des jambes et l'endurance.",durée:"8 semaines",prix:"160€",photo_url:"https://images.unsplash.com/photo-1615845522846-02f89af04c2e?q=80&w=1938&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",sport:"Cyclisme"},{titre:"Danse Fitness",description:"Un programme fun et dynamique mélangeant des mouvements de danse et des exercices de cardio, parfait pour s'amuser tout en restant en forme.",durée:"6 semaines",prix:"90€",photo_url:"https://images.unsplash.com/photo-1611077094726-11cf1f992009?q=80&w=2069&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",sport:"Danse"},{titre:"Entraînement en Piscine",description:"Un programme complet de natation pour améliorer la technique, l'endurance et la force musculaire.",durée:"7 semaines",prix:"150€",photo_url:"https://images.unsplash.com/photo-1519315901367-f34ff9154487?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",sport:"Natation"}]);return(g,h)=>(i(),p(o(I),{"data-page":"Program"},{default:s(()=>[a(o(C),null,{default:s(()=>[L,e("div",z,[J,e("div",K,[(i(!0),f(M,null,B(t.value,y=>(i(),p(o(b),null,{default:s(()=>[m(n(y),1)]),_:2},1024))),256))]),O]),a(_,{programs:l.value},null,8,["programs"]),Q,a(_,{programs:d.value},null,8,["programs"])]),_:1})]),_:1}))}}),te=x(X,[["__scopeId","data-v-315c2cdf"]]);export{te as default};
