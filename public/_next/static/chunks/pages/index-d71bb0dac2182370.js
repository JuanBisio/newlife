(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[405],{5557:function(e,t,n){(window.__NEXT_P=window.__NEXT_P||[]).push(["/",function(){return n(43)}])},43:function(e,t,n){"use strict";n.r(t),n.d(t,{Box_346498bdf26ce4b6c5e6aa3b132431a7:function(){return Box_346498bdf26ce4b6c5e6aa3b132431a7},Button_3160885b8073141b7ab9cb4db40030c8:function(){return Button_3160885b8073141b7ab9cb4db40030c8},Button_5ddbfc051c7e404130ec2debdc115b8c:function(){return Button_5ddbfc051c7e404130ec2debdc115b8c},Button_c69cb7a05966693f990c76e7d7c33828:function(){return Button_c69cb7a05966693f990c76e7d7c33828},Debounceinput_0ad29a48b4ae4e6988dc57eddb8237a7:function(){return Debounceinput_0ad29a48b4ae4e6988dc57eddb8237a7},Input_366d732364755d4b0607fb9e56eae93f:function(){return Input_366d732364755d4b0607fb9e56eae93f},Input_56acdcb2766fb456aba24b54324d32cb:function(){return Input_56acdcb2766fb456aba24b54324d32cb},Modal_15a66c49aa4f06bebd8fd6ef9f74fffd:function(){return Modal_15a66c49aa4f06bebd8fd6ef9f74fffd},Modal_8eee44d5c248b401d36923b3e2924cb0:function(){return Modal_8eee44d5c248b401d36923b3e2924cb0},Modal_fc081c85e1c49f0643ca9924035ee00c:function(){return Modal_fc081c85e1c49f0643ca9924035ee00c},default:function(){return Component}});var o=n(6811),r=n(7294),a=n(8595),i=n(9222),d=n(8129),s=n(1753),c=n(2752),l=n(1963),h=n(1948),m=n(4504),u=n(7822),b=n(3793),f=n(7018),x=n(3100),g=n(4418),p=n(1669),C=n(8570),Z=n(4641),F=n(4416),_=n(5034),w=n(3838),A=n(8911),y=n(7754),v=n(4298),D=n.n(v);n(5202);var z=n(1664),k=n.n(z),X=n(738),B=n(687),R=n(6608),E=n(775),S=n(9008),I=n.n(S);function Button_5ddbfc051c7e404130ec2debdc115b8c(){let[e,t]=(0,r.useContext)(B.DR),n=(0,r.useCallback)(t=>e([(0,R.ju)("state.modal_state.change",{})],t,{}),[e,R.ju]);return(0,o.tZ)(i.z,{onClick:n,sx:{width:"100%",height:"2.5em",borderRadius:"0.5em",bg:"#D3A514",_hover:{backgroundColor:"#1C1C1A"},margin:".7em"},children:"Kimax"})}function Input_56acdcb2766fb456aba24b54324d32cb(){let[e,t]=(0,r.useContext)(B.DR),n=(0,r.useCallback)(t=>e([(0,R.ju)("state.registration_form_error_state.set_name",{value:t.target.value})],t,{}),[e,R.ju]);return(0,o.tZ)(d.I,{errorBorderColor:"#777771",focusBorderColor:"#D3A514",name:"Nombre: ",onBlur:n,placeholder:"Nombre",sx:{border:"1px dotted #777771",_hover:{border:"1px dotted #D3A514"}},type:"text"})}function Debounceinput_0ad29a48b4ae4e6988dc57eddb8237a7(){let e=(0,r.useContext)(B.M4.state__registration_textarea_state),[t,n]=(0,r.useContext)(B.DR),a=(0,r.useCallback)(e=>t([(0,R.ju)("state.registration_textarea_state.set_text",{value:e.target.value})],e,{}),[t,R.ju]);return(0,o.tZ)(E.DebounceInput,{debounceTimeout:50,element:s.g,focusBorderColor:"#D3A514",name:"Mensaje: ",onChange:a,sx:{border:"1px dotted #777771",_hover:{border:"1px dotted #D3A514"},marginY:"1em"},value:e.text})}function Modal_15a66c49aa4f06bebd8fd6ef9f74fffd(){let e=(0,r.useContext)(B.M4.state__modal_state);return(0,o.tZ)(c.u_,{isOpen:e.show,sx:{width:"30em",height:"30em"},children:(0,o.tZ)(l.Z,{children:(0,o.BX)(h.h,{sx:{bg:"#1C1C1A"},children:[(0,o.BX)(m.x,{children:["Kimax",(0,o.tZ)(u.i,{})]}),(0,o.tZ)(b.f,{children:"KI MAX \xae se practica con una bolsa de pie exclusivamente dise\xf1ada, con guantes para pegar a la bolsa. (Traer vendas y/o guantes) Los “Rounds” de KI MAX \xae implementan t\xe9cnicas de Boxeo, Muay Thai y Kickboxing a trav\xe9s de combinaciones simples, intensas y din\xe1micas."}),(0,o.tZ)(f.m,{children:(0,o.tZ)(a.qh,{})})]})})})}function Input_366d732364755d4b0607fb9e56eae93f(){let[e,t]=(0,r.useContext)(B.DR),n=(0,r.useCallback)(t=>e([(0,R.ju)("state.registration_form_error_state.set_name",{value:t.target.value})],t,{}),[e,R.ju]);return(0,o.tZ)(d.I,{errorBorderColor:"#777771",focusBorderColor:"#D3A514",name:"Apellido: ",onBlur:n,placeholder:"Apellido",sx:{border:"1px dotted #777771",_hover:{border:"1px dotted #D3A514"}},type:"text"})}function Box_346498bdf26ce4b6c5e6aa3b132431a7(){let e=(0,r.useCallback)(e=>{let n=e.target;e.preventDefault();let o={...Object.fromEntries(new FormData(n).entries())};t([(0,R.ju)("state.registration_form_state.handle_submit",{form_data:o})])}),[t,n]=(0,r.useContext)(B.DR);return(0,o.BX)(x.xu,{as:"form",onSubmit:e,sx:{width:["20em","15em","15em","20em","30em"]},children:[(0,o.tZ)(Input_56acdcb2766fb456aba24b54324d32cb,{}),(0,o.tZ)(Input_366d732364755d4b0607fb9e56eae93f,{}),(0,o.tZ)(g.X,{size:"lg",sx:{color:"#D3A514",marginY:"0.5em"},children:"Clases"}),(0,o.BX)(p.g,{alignItems:"left",justifyContent:"left",sx:{display:"flex",textAling:"left"},children:[(0,o.tZ)(C.X,{colorScheme:"yellow",name:"Localizada",size:"md",value:"true",children:"Localizada"}),(0,o.tZ)(C.X,{colorScheme:"yellow",name:"Kimax",size:"md",value:"true",children:"Kimax"}),(0,o.tZ)(C.X,{colorScheme:"yellow",name:"Full Hit",size:"md",value:"true",children:"Full Hit"}),(0,o.tZ)(C.X,{colorScheme:"yellow",name:"Karate",size:"md",value:"true",children:"Karate"}),(0,o.tZ)(C.X,{colorScheme:"yellow",name:"Piernas/Abdominales",size:"md",value:"true",children:"Piernas/Abdominales"}),(0,o.tZ)(C.X,{colorScheme:"yellow",name:"Ritmos Latinos",size:"md",value:"true",children:"Ritmos Latinos"}),(0,o.tZ)(C.X,{colorScheme:"yellow",name:"Kimax",size:"md",value:"true",children:"Piernas/Gluteos"}),(0,o.tZ)(C.X,{colorScheme:"yellow",name:"Power Flex",size:"md",value:"true",children:"Power Flex"}),(0,o.tZ)(C.X,{colorScheme:"yellow",name:"Entrenamiento Funcional",size:"md",value:"true",children:"Entrenamiento Funcional"}),(0,o.tZ)(C.X,{colorScheme:"yellow",name:"Power",size:"md",value:"true",children:"Power"}),(0,o.tZ)(C.X,{colorScheme:"yellow",name:"Musculacion",size:"md",value:"true",children:"Musculacion"})]}),(0,o.tZ)(Debounceinput_0ad29a48b4ae4e6988dc57eddb8237a7,{}),(0,o.tZ)(Z.U,{children:(0,o.tZ)(i.z,{sx:{bg:"#D3A514",color:"#FFFFFF",_hover:{transform:"scale(1.1)"}},type:"submit",children:"Enviar a Whatsapp"})})]})}function Modal_8eee44d5c248b401d36923b3e2924cb0(){let e=(0,r.useContext)(B.M4.state__modal_state);return(0,o.tZ)(c.u_,{isOpen:e.show,sx:{width:"30em",height:"30em"},children:(0,o.tZ)(l.Z,{children:(0,o.BX)(h.h,{sx:{bg:"#1C1C1A"},children:[(0,o.BX)(m.x,{children:["Karate",(0,o.tZ)(u.i,{})]}),(0,o.tZ)(b.f,{children:"El karate es un arte marcial de origen japon\xe9s que consiste en la defensa personal. Su pr\xe1ctica tiene beneficios a nivel f\xedsico y mental. La disciplina es un elemento esencial para practicar karate. Aprende una nueva filosof\xeda de vida. Clases para ni\xf1os, adolescentes y adultos"}),(0,o.tZ)(f.m,{children:(0,o.tZ)(a.qh,{})})]})})})}function Button_3160885b8073141b7ab9cb4db40030c8(){let[e,t]=(0,r.useContext)(B.DR),n=(0,r.useCallback)(t=>e([(0,R.ju)("state.modal_state.change",{})],t,{}),[e,R.ju]);return(0,o.tZ)(i.z,{onClick:n,sx:{width:"100%",height:"2.5em",borderRadius:"0.5em",bg:"#D3A514",_hover:{backgroundColor:"#1C1C1A"},margin:".7em"},children:"Karate"})}function Button_c69cb7a05966693f990c76e7d7c33828(){let[e,t]=(0,r.useContext)(B.DR),n=(0,r.useCallback)(t=>e([(0,R.ju)("state.modal_state.change",{})],t,{}),[e,R.ju]);return(0,o.tZ)(i.z,{onClick:n,sx:{width:"100%",height:"2.5em",borderRadius:"0.5em",bg:"#D3A514",_hover:{backgroundColor:"#1C1C1A"},margin:".7em"},children:"Localizada"})}function Modal_fc081c85e1c49f0643ca9924035ee00c(){let e=(0,r.useContext)(B.M4.state__modal_state);return(0,o.tZ)(c.u_,{isOpen:e.show,sx:{width:"30em",height:"30em"},children:(0,o.tZ)(l.Z,{children:(0,o.BX)(h.h,{sx:{bg:"#1C1C1A"},children:[(0,o.BX)(m.x,{children:["Localizada",(0,o.tZ)(u.i,{})]}),(0,o.tZ)(b.f,{children:"En esta clase vas a realizar trabajos de fuerza y resistencia muscular, utilizando diversos elementos con movimientos coordinativos b\xe1sicos. Trabajamos con bandas, mancuernas, tobilleras, barras y discos, colchonetas, con el objetivo de aumentar la resistencia y fuerza muscular.    "}),(0,o.tZ)(f.m,{children:(0,o.tZ)(a.qh,{})})]})})})}function Component(){let e=(0,r.useRef)(null);R.xL.ref_galery=e;let t=(0,r.useRef)(null);return R.xL.ref_footer=t,(0,o.BX)(r.Fragment,{children:[(0,o.tZ)(a.gv,{}),(0,o.BX)(x.xu,{sx:{fontFamily:"Roboto",color:"#FFFFFF",background:"#1C1C1A",scrollBehavior:"smooth"},children:[(0,o.tZ)(D(),{strategy:"afterInteractive",children:"document.documentElement.lang='es'"}),(0,o.BX)(p.g,{sx:{bg:"#1C1C1A",position:"sticky",paddingX:"2em",paddingY:"0.5em",zIndex:"999",top:"0",width:"100%",fontFamily:"Roboto"},children:[(0,o.BX)(Z.U,{sx:{width:"100%"},children:[(0,o.tZ)(F.E,{alt:"Logo de New Life Gym",src:"/header/LogoR.webp",sx:{width:"14em",height:"4em"}}),(0,o.tZ)(_.L,{}),(0,o.tZ)(x.xu,{sx:{display:["none","none","none","block"]},children:(0,o.BX)(Z.U,{children:[(0,o.tZ)(w.r,{as:k(),href:"/",isExternal:!1,sx:{paddingX:".2em",textDecoration:"none"},children:(0,o.tZ)(i.z,{sx:{bg:"none",_hover:{backgroundColor:"#FFFFFF00",color:"#D3A514"},fontSize:"1.05em",fontFamily:"Roboto Condensed"},children:"Newlife"})}),(0,o.tZ)(w.r,{as:k(),href:"/instalaciones",isExternal:!1,sx:{paddingX:".2em",textDecoration:"none"},children:(0,o.tZ)(i.z,{sx:{bg:"none",_hover:{backgroundColor:"#FFFFFF00",color:"#D3A514"},fontSize:"1.05em",fontFamily:"Roboto Condensed"},children:"Instalaciones"})}),(0,o.tZ)(w.r,{as:k(),href:"/actividades",isExternal:!1,sx:{paddingX:".2em",textDecoration:"none"},children:(0,o.tZ)(i.z,{sx:{bg:"none",_hover:{backgroundColor:"#FFFFFF00",color:"#D3A514"},fontSize:"1.05em",fontFamily:"Roboto Condensed"},children:"Actividades"})}),(0,o.tZ)(w.r,{as:k(),href:"/horarios",isExternal:!1,sx:{paddingX:".2em",textDecoration:"none"},children:(0,o.tZ)(i.z,{sx:{bg:"none",_hover:{backgroundColor:"#FFFFFF00",color:"#D3A514"},fontSize:"1.05em",fontFamily:"Roboto Condensed"},children:"Horarios"})})]})}),(0,o.tZ)(_.L,{}),(0,o.tZ)(x.xu,{sx:{display:["block","block","block","none"]},children:(0,o.BX)(x.xu,{children:[(0,o.tZ)(a.t5,{}),(0,o.tZ)(a.zw,{})]})}),(0,o.tZ)(x.xu,{sx:{display:["none","none","none","block"]},children:(0,o.BX)(Z.U,{children:[(0,o.tZ)(w.r,{as:k(),href:"https://www.instagram.com/newlifegimnasio/",isExternal:!0,sx:{paddingX:".2em",textDecoration:"none"},children:(0,o.tZ)(i.z,{sx:{bg:"none",_hover:{backgroundColor:"#D3A514",color:"#D3A514"},fontSize:"1.05em",fontFamily:"Roboto Condensed"},children:(0,o.tZ)(F.E,{src:"/iconsImage/instagram.webp",sx:{width:"1em",height:"1em"}})})}),(0,o.tZ)(w.r,{as:k(),href:"https://api.whatsapp.com/send/?phone=5493584299645&text&app_absent=0",isExternal:!0,sx:{paddingX:".2em",textDecoration:"none"},children:(0,o.tZ)(i.z,{sx:{bg:"none",_hover:{backgroundColor:"#D3A514",color:"#D3A514"},fontSize:"1.05em",fontFamily:"Roboto Condensed"},children:(0,o.tZ)(F.E,{src:"/iconsImage/whatsapp.webp",sx:{width:"1em",height:"1em"}})})}),(0,o.tZ)(w.r,{as:k(),href:"https://www.facebook.com/newliferiocuarto/",isExternal:!0,sx:{paddingX:".2em",textDecoration:"none"},children:(0,o.tZ)(i.z,{sx:{bg:"none",_hover:{backgroundColor:"#D3A514",color:"#D3A514"},fontSize:"1.05em",fontFamily:"Roboto Condensed"},children:(0,o.tZ)(F.E,{src:"/iconsImage/facebook.webp",sx:{width:"1em",height:"1em"}})})}),(0,o.tZ)(w.r,{as:k(),href:"https://twitter.com/newlifegimnasio",isExternal:!0,sx:{paddingX:".2em",textDecoration:"none"},children:(0,o.tZ)(i.z,{sx:{bg:"none",_hover:{backgroundColor:"#D3A514",color:"#D3A514"},fontSize:"1.05em",fontFamily:"Roboto Condensed"},children:(0,o.tZ)(F.E,{src:"/iconsImage/twitter.webp",sx:{width:"1em",height:"1em"}})})})]})})]}),(0,o.tZ)(X.Z,{badge:{dot:!0,color:"#D3A514"},colorFillContent:"#1C1C1A",href:"https://api.whatsapp.com/send/?phone=5493584299645&text&app_absent=0",icon:(0,o.tZ)(F.E,{src:"/iconsImage/WhatsappB.webp",sx:{width:"24px",height:"auto"}}),target:"_blank"})]}),(0,o.tZ)(Z.U,{sx:{backgroundImage:[["/header/FondoMobile.webp"],["/header/FondoTablet.webp"],["/header/FondoLaptop.webp"],["/header/FondoLaptop.webp"],["/header/CompressFondo3.webp"]],backgroundSize:"cover",backgroundAttachment:"fixed",backgroundPosition:"center"},children:(0,o.tZ)(Z.U,{alignItems:"center",justifyContent:"left",sx:{display:"flex",width:"100%",height:"89vh",margin:"0px !important",fontFamily:"Roboto Condensed",bg:"#1C1C1ACC"},children:(0,o.BX)(p.g,{alignItems:"left",justifyContent:"left",sx:{display:"flex",textAling:"left",marginX:"2em",maxWidth:["90%","90%","70%","30%","30%"]},children:[(0,o.tZ)(A.x,{sx:{fontSize:"1.7em",color:"#D3A514",marginBottom:"0px",paddingBottom:"0px"},children:"La transformacion de tu vida inicia aqui"}),(0,o.tZ)(A.x,{sx:{fontSize:"1em",color:"#FFFFFF",marginBottom:"5px",paddingBottom:"0px"},children:"Desaf\xeda tu limites y comienza ahora una nueva vida mas saludable, din\xe1mica y divertida. Con tan solo 45 minutos de actividad puedes conseguir resultados incre\xedbles. Tenemos varias opciones en nuestros horarios. Encuentra la mejor propuesta para ti y ven a entrenar con nosotros."}),(0,o.tZ)(w.r,{as:k(),href:"#galery",children:(0,o.tZ)(i.z,{sx:{bg:"#D3A514",borderRadius:"5px",width:"50%",_hover:{backgroundColor:"#1C1C1A"}},children:"EMPEZAR"})})]})})}),(0,o.tZ)(y.M,{sx:{bg:"#1C1C1A",paddingTop:"2em"},children:(0,o.BX)(p.g,{sx:{color:"#FFFFFF",textAling:"center",fontFamily:"Roboto",maxWidth:"800px",padding:"2em"},children:[(0,o.tZ)(g.X,{size:"xl",sx:{color:"#D3A514",margin:"0.5em",fontFamily:"Syne"},children:"VEN\xcd A CONOCERNOS"}),(0,o.tZ)(g.X,{size:"lg",sx:{color:"#D3A514",margin:"1em",paddingBottom:"0.5em",fontFamily:"Syne"},children:"\xa1Transform\xe1 tu vida desde hoy!"}),(0,o.tZ)(A.x,{sx:{textAling:"center",paddingBottom:"0.5em"},children:"New Life ha ayudado a generar cambios positivos en la vida de sus clientes, en R\xedo Cuarto, desde su fundaci\xf3n en el a\xf1o 1987. Creemos que el entrenamiento f\xedsico no es solo un pasatiempo sino un estilo de vida. Creamos nuestro gimnasio para que sea el segundo hogar de todos nuestros usuarios. Ya sea que realices actividad f\xedsica todos los d\xedas o que nunca hayas ido a un gimnasio antes, New Life puede ayudar a darle forma en lo que puedes convertirte ma\xf1ana. Queremos ser aliados de tu entrenamiento."}),(0,o.tZ)(A.x,{sx:{textAling:"center",paddingBottom:"0.5em"},children:"\xa1Alcanz\xe1 tus metas y disfruta de tu nueva vida!"}),(0,o.BX)(Z.U,{justifyContent:"space_evenly",sx:{display:"flex"},children:[(0,o.tZ)(w.r,{as:k(),href:"#footer",children:(0,o.tZ)(i.z,{sx:{bg:"#D3A514",borderRadius:"5px",color:"#FFFFFF",_hover:{transform:"scale(1.1)"}},children:"Contactar"})}),(0,o.tZ)(_.L,{}),(0,o.tZ)(w.r,{as:k(),href:"/horarios",children:(0,o.tZ)(i.z,{sx:{bg:"#D3A514",borderRadius:"5px",color:"#FFFFFF",_hover:{transform:"scale(1.1)"}},children:"Horarios"})})]})]})}),(0,o.tZ)(p.g,{sx:{bg:"#1C1C1A",width:"100%",height:"6em"}}),(0,o.tZ)(y.M,{sx:{bg:"#1C1C1A"},children:(0,o.BX)(p.g,{children:[(0,o.tZ)(g.X,{size:"2xl",sx:{fontFamily:"Syne",margin:"0.5em",color:"#D3A514"},children:"\xbfCU\xc1L ES TU META?"}),(0,o.BX)(x.xu,{sx:{maxWidth:"1000px",display:"flex",flexDirection:["column","column","column","row","row"]},children:[(0,o.BX)(x.xu,{sx:{display:"flex",justifyContent:"center",alignItems:"end",backgroundImage:"/galery/Kimax.webp",backgroundPosition:"center",backgroundSize:"cover",transition:"0.5s",_hover:{transform:"scale(1.1)"},width:"20em",height:"30em",border:"#D3A514",borderRadius:"1em",margin:"1em"},children:[(0,o.tZ)(Button_c69cb7a05966693f990c76e7d7c33828,{}),(0,o.tZ)(Modal_fc081c85e1c49f0643ca9924035ee00c,{})]}),(0,o.tZ)(_.L,{}),(0,o.BX)(x.xu,{sx:{display:"flex",justifyContent:"center",alignItems:"end",backgroundImage:"/galery/CompressFondo1.webp",backgroundPosition:"center",backgroundSize:"cover",transition:"0.5s",_hover:{transform:"scale(1.1)"},width:"20em",height:"30em",border:"#D3A514",borderRadius:"1em",margin:"1em"},children:[(0,o.tZ)(Button_5ddbfc051c7e404130ec2debdc115b8c,{}),(0,o.tZ)(Modal_15a66c49aa4f06bebd8fd6ef9f74fffd,{})]}),(0,o.tZ)(_.L,{}),(0,o.BX)(x.xu,{sx:{display:"flex",justifyContent:"center",alignItems:"end",backgroundImage:"/galery/Karate.webp",backgroundPosition:"center",backgroundSize:"cover",transition:"0.5s",_hover:{transform:"scale(1.1)"},width:"20em",height:"30em",border:"#D3A514",borderRadius:"1em",margin:"1em"},children:[(0,o.tZ)(Button_3160885b8073141b7ab9cb4db40030c8,{}),(0,o.tZ)(Modal_8eee44d5c248b401d36923b3e2924cb0,{})]})]})]})}),(0,o.tZ)(p.g,{sx:{bg:"#1C1C1A",width:"100%",height:"6em"}}),(0,o.tZ)(y.M,{sx:{bg:"#1C1C1A"},children:(0,o.BX)(p.g,{sx:{maxWidth:"1200px"},children:[(0,o.tZ)(g.X,{size:"2xl",sx:{fontFamily:"Syne",margin:"0.5em",color:"#D3A514"},children:"DESCARGA LA APP"}),(0,o.tZ)(Z.U,{children:(0,o.tZ)(w.r,{as:k(),href:"https://play.google.com/store/apps/details?id=com.socioplus&hl=es_AR&gl=US&pli=1",isExternal:!0,children:(0,o.tZ)(F.E,{src:"/app/iphone.png"})})})]})}),(0,o.tZ)(p.g,{sx:{bg:"#1C1C1A",width:"100%",height:"6em"}}),(0,o.tZ)(y.M,{id:"galery",ref:e,sx:{bg:"#1C1C1A",overflow:"overview"},children:(0,o.BX)(p.g,{sx:{maxWidth:"1200px"},children:[(0,o.tZ)(g.X,{size:"2xl",sx:{fontFamily:"Syne",margin:"0.5em",color:"#D3A514"},children:"\xa1COMIENZA TU EXPERIENCIA AHORA!"}),(0,o.tZ)(p.g,{children:(0,o.tZ)(Box_346498bdf26ce4b6c5e6aa3b132431a7,{})})]})}),(0,o.tZ)(p.g,{sx:{bg:"#1C1C1A",width:"100%",height:"6em"}}),(0,o.tZ)(y.M,{sx:{bg:"#1C1C1A"},children:(0,o.BX)(p.g,{sx:{maxWidth:"1200px"},children:[(0,o.tZ)(x.xu,{sx:{display:["none","none","none","block"]},children:(0,o.tZ)(x.xu,{dangerouslySetInnerHTML:{__html:'<iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d6682.547276147136!2d-64.358636!3d-33.128175!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95d200166883e809%3A0xbdb203d7d982775!2sMar%C3%ADa%20Olguin%201324%2C%20X5800%20R%C3%ADo%20Cuarto%2C%20C%C3%B3rdoba%2C%20Argentina!5e0!3m2!1ses-419!2sus!4v1707879795092!5m2!1ses-419!2sus" width="1140" height="534" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'}})}),(0,o.tZ)(x.xu,{sx:{display:["block","block","block","none"]},children:(0,o.tZ)(x.xu,{dangerouslySetInnerHTML:{__html:'<iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d26729.565413549644!2d-64.3455468!3d-33.1302235!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95d200166883e809%3A0xbdb203d7d982775!2sMar%C3%ADa%20Olguin%201324%2C%20X5800%20R%C3%ADo%20Cuarto%2C%20C%C3%B3rdoba%2C%20Argentina!5e0!3m2!1ses-419!2sus!4v1707931235099!5m2!1ses-419!2sus" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'}})})]})}),(0,o.tZ)(p.g,{sx:{bg:"#1C1C1A",width:"100%",height:"6em"}}),(0,o.tZ)(p.g,{sx:{bg:"#1C1C1A",width:"100%",height:"6em"}}),(0,o.BX)(p.g,{id:"footer",ref:t,sx:{bg:"#1C1C1A",position:"sticky",paddingX:"2em",paddingY:"0.5em",zIndex:"999",top:"0",width:"100%",fontFamily:"Roboto"},children:[(0,o.BX)(Z.U,{sx:{width:"100%"},children:[(0,o.tZ)(x.xu,{sx:{display:["none","none","none","block"]},children:(0,o.BX)(Z.U,{children:[(0,o.tZ)(w.r,{as:k(),href:"/",isExternal:!1,sx:{paddingX:".2em",textDecoration:"none"},children:(0,o.tZ)(i.z,{sx:{bg:"none",_hover:{backgroundColor:"#FFFFFF00",color:"#D3A514"},fontSize:"1.05em",fontFamily:"Roboto Condensed"},children:"Newlife"})}),(0,o.tZ)(w.r,{as:k(),href:"/instalaciones",isExternal:!1,sx:{paddingX:".2em",textDecoration:"none"},children:(0,o.tZ)(i.z,{sx:{bg:"none",_hover:{backgroundColor:"#FFFFFF00",color:"#D3A514"},fontSize:"1.05em",fontFamily:"Roboto Condensed"},children:"Instalaciones"})}),(0,o.tZ)(w.r,{as:k(),href:"/actividades",isExternal:!1,sx:{paddingX:".2em",textDecoration:"none"},children:(0,o.tZ)(i.z,{sx:{bg:"none",_hover:{backgroundColor:"#FFFFFF00",color:"#D3A514"},fontSize:"1.05em",fontFamily:"Roboto Condensed"},children:"Actividades"})}),(0,o.tZ)(w.r,{as:k(),href:"/suplementos",isExternal:!1,sx:{paddingX:".2em",textDecoration:"none"},children:(0,o.tZ)(i.z,{sx:{bg:"none",_hover:{backgroundColor:"#FFFFFF00",color:"#D3A514"},fontSize:"1.05em",fontFamily:"Roboto Condensed"},children:"Horarios"})})]})}),(0,o.tZ)(x.xu,{sx:{display:["block","block","block","none"]},children:(0,o.BX)(x.xu,{children:[(0,o.tZ)(a.t5,{}),(0,o.tZ)(a.zw,{})]})}),(0,o.tZ)(_.L,{}),(0,o.BX)(Z.U,{children:[(0,o.tZ)(A.x,{sx:{color:"#FFFFFF",fontSize:"1.5em"},children:"This is"}),(0,o.tZ)(A.x,{sx:{color:"#D3A514",fontSize:"1.5em"},children:"New Life"})]}),(0,o.tZ)(_.L,{}),(0,o.tZ)(x.xu,{sx:{display:["none","none","none","block"]},children:(0,o.BX)(Z.U,{children:[(0,o.tZ)(w.r,{as:k(),href:"https://www.instagram.com/newlifegimnasio/",isExternal:!0,sx:{paddingX:".2em",textDecoration:"none"},children:(0,o.tZ)(i.z,{sx:{bg:"none",_hover:{backgroundColor:"#D3A514",color:"#D3A514"},fontSize:"1.05em",fontFamily:"Roboto Condensed"},children:(0,o.tZ)(F.E,{src:"/iconsImage/instagram.webp",sx:{width:"1em",height:"1em"}})})}),(0,o.tZ)(w.r,{as:k(),href:"https://api.whatsapp.com/send/?phone=5493584299645&text&app_absent=0",isExternal:!0,sx:{paddingX:".2em",textDecoration:"none"},children:(0,o.tZ)(i.z,{sx:{bg:"none",_hover:{backgroundColor:"#D3A514",color:"#D3A514"},fontSize:"1.05em",fontFamily:"Roboto Condensed"},children:(0,o.tZ)(F.E,{src:"/iconsImage/whatsapp.webp",sx:{width:"1em",height:"1em"}})})}),(0,o.tZ)(w.r,{as:k(),href:"https://www.facebook.com/newliferiocuarto/",isExternal:!0,sx:{paddingX:".2em",textDecoration:"none"},children:(0,o.tZ)(i.z,{sx:{bg:"none",_hover:{backgroundColor:"#D3A514",color:"#D3A514"},fontSize:"1.05em",fontFamily:"Roboto Condensed"},children:(0,o.tZ)(F.E,{src:"/iconsImage/facebook.webp",sx:{width:"1em",height:"1em"}})})}),(0,o.tZ)(w.r,{as:k(),href:"https://twitter.com/newlifegimnasio",isExternal:!0,sx:{paddingX:".2em",textDecoration:"none"},children:(0,o.tZ)(i.z,{sx:{bg:"none",_hover:{backgroundColor:"#D3A514",color:"#D3A514"},fontSize:"1.05em",fontFamily:"Roboto Condensed"},children:(0,o.tZ)(F.E,{src:"/iconsImage/twitter.webp",sx:{width:"1em",height:"1em"}})})})]})})]}),(0,o.tZ)(X.Z,{badge:{dot:!0,color:"#D3A514"},colorFillContent:"#1C1C1A",href:"https://api.whatsapp.com/send/?phone=5493584299645&text&app_absent=0",icon:(0,o.tZ)(F.E,{src:"/iconsImage/WhatsappB.webp",sx:{width:"24px",height:"auto"}}),target:"_blank"})]})]}),(0,o.BX)(I(),{children:[(0,o.tZ)("title",{children:"New Life"}),(0,o.tZ)("meta",{content:"Brindamos propuestas de entrenamiento seg\xfan objetivos y necesidades a personas que buscan bienestar y salud. Maria Olguin 1324, R\xedo Cuarto 5800.",name:"description"}),(0,o.tZ)("meta",{content:"/icons/newlife.png",property:"og:image"})]})]})}},8595:function(e,t,n){"use strict";n.d(t,{gv:function(){return Fragment_fd0e7cb8f9fb4669a6805377d925fba0},qh:function(){return Button_bbc7ae16209f731a2271f035f8be5379},t5:function(){return Button_32087f559e1a6b8973b973facea8f3be},zw:function(){return Drawer_62c8b8862581b385087a81a42afb4f59}});var o=n(6811),r=n(7294),a=n(687),i=n(6608),d=n(2752),s=n(1963),c=n(1948),l=n(4504),h=n(3793),m=n(8911),u=n(9222),b=n(5972),f=n(1085),x=n(1669),g=n(3838),p=n(7018);n(5202);var C=n(3151),Z=n(1664),F=n.n(Z);function Fragment_fd0e7cb8f9fb4669a6805377d925fba0(){let[e,t]=(0,r.useContext)(a.DR);return(0,o.tZ)(r.Fragment,{children:(0,i.oA)(null!==t)?(0,o.tZ)(r.Fragment,{children:(0,o.tZ)(d.u_,{isOpen:null!==t,children:(0,o.tZ)(s.Z,{children:(0,o.BX)(c.h,{children:[(0,o.tZ)(l.x,{children:"Connection Error"}),(0,o.tZ)(h.f,{children:(0,o.BX)(m.x,{children:["Cannot connect to server: ",null!==t?t.message:"",". Check if server is reachable at ",(0,i.e9)().href]})})]})})})}):(0,o.tZ)(r.Fragment,{})})}function Button_32087f559e1a6b8973b973facea8f3be(){let[e,t]=(0,r.useContext)(a.DR),n=(0,r.useCallback)(t=>e([(0,i.ju)("state.drawer_state.right",{})],t,{}),[e,i.ju]);return(0,o.tZ)(u.z,{onClick:n,sx:{bg:"none",_hover:{backgroundColor:"#D3A514"}},children:(0,o.tZ)(C.U,{sx:{width:"1.25em",height:"1.25em"}})})}function Button_59e24e1cc21fb455d131022ee2de186a(){let[e,t]=(0,r.useContext)(a.DR),n=(0,r.useCallback)(t=>e([(0,i.ju)("state.drawer_state.right",{})],t,{}),[e,i.ju]);return(0,o.tZ)(u.z,{onClick:n,sx:{bg:"#D3A514"},children:"Cerrar"})}function Drawer_62c8b8862581b385087a81a42afb4f59(){let e=(0,r.useContext)(a.M4.state__drawer_state);return(0,o.tZ)(b.d,{isOpen:e.show_right,children:(0,o.tZ)(s.Z,{children:(0,o.BX)(f.s,{sx:{bg:"#1C1C1ACC"},children:[(0,o.tZ)(l.x,{sx:{display:"flex",justifyContent:"center",fontSize:"1.7em",color:"#D3A514"},children:"New Life"}),(0,o.tZ)(h.f,{sx:{fontSize:"1.25em",display:"flex",justifyContent:"center"},children:(0,o.BX)(x.g,{children:[(0,o.tZ)(g.r,{as:F(),href:"/",isExternal:!1,sx:{paddingX:".2em",textDecoration:"none"},children:(0,o.tZ)(u.z,{sx:{bg:"none",_hover:{backgroundColor:"#FFFFFF00",color:"#D3A514"},fontSize:"1.05em",fontFamily:"Roboto Condensed"},children:"Newlife"})}),(0,o.tZ)(g.r,{as:F(),href:"/instalaciones",isExternal:!1,sx:{paddingX:".2em",textDecoration:"none"},children:(0,o.tZ)(u.z,{sx:{bg:"none",_hover:{backgroundColor:"#FFFFFF00",color:"#D3A514"},fontSize:"1.05em",fontFamily:"Roboto Condensed"},children:"Instalaciones"})}),(0,o.tZ)(g.r,{as:F(),href:"/actividades",isExternal:!1,sx:{paddingX:".2em",textDecoration:"none"},children:(0,o.tZ)(u.z,{sx:{bg:"none",_hover:{backgroundColor:"#FFFFFF00",color:"#D3A514"},fontSize:"1.05em",fontFamily:"Roboto Condensed"},children:"Actividades"})}),(0,o.tZ)(g.r,{as:F(),href:"/horarios",isExternal:!1,sx:{paddingX:".2em",textDecoration:"none"},children:(0,o.tZ)(u.z,{sx:{bg:"none",_hover:{backgroundColor:"#FFFFFF00",color:"#D3A514"},fontSize:"1.05em",fontFamily:"Roboto Condensed"},children:"Horarios"})})]})}),(0,o.tZ)(p.m,{children:(0,o.tZ)(Button_59e24e1cc21fb455d131022ee2de186a,{})})]})})})}function Button_bbc7ae16209f731a2271f035f8be5379(){let[e,t]=(0,r.useContext)(a.DR),n=(0,r.useCallback)(t=>e([(0,i.ju)("state.modal_state.change",{})],t,{}),[e,i.ju]);return(0,o.tZ)(u.z,{onClick:n,sx:{bg:"#D3A514",_hover:{backgroundColor:"#5F2C23DD"}},children:"Cerrar"})}}},function(e){e.O(0,[431,752,518,774,888,179],function(){return e(e.s=5557)}),_N_E=e.O()}]);