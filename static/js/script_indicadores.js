/* el querySelector nos permite seleccionar para
manipular un componente de la página */
document.querySelector("#dolar").addEventListener(
    'click', function(){
        obtener_datos('dolar');
    }
    );
    
    function obtener_datos(valor){
        let url ='https://mindicador.cl/api/'+valor;
        //este objeto nos permite leer la api
        const api= new XMLHttpRequest();
        api.open('GET', url, true);
        api.send();
        // El "onreadystatechange" especifica a la 
        //la funcion que se ejecutarpá cada vez que 
        //cambie el estado de objeto XMLHttpRequest        
        api.onreadystatechange= function(){
            //estas indicaciones con para la validar
            //la correcta solicitud y la correcta respuesta
            if(this.status==200 && this.readyState==4){
                let datos= JSON.parse(this.responseText);
               // console.log(datos.autor);
               // console.log(datos.nombre);
               var autor= datos.autor;
               $("#autor").html(autor);
               $("#nombre").html(datos.nombre);
               $("#unidad_medida").html(datos.unidad_medida);
               // nuevamente usaremos el querySelector
               let resultado=
               document.querySelector("#desplegar-tabla");
               // vamos a limpiar antes de desplegar
               resultado.innerHTML="";
               //ahora debemos recorrer la key "serie"
               // dle JSon porque esta es una colección
               for(let item of datos.serie){
                   resultado.innerHTML+=" $"+item.valor+
                   "  Fecha:"+
                   item.fecha.substring(0,10)+"<br>";
               }
    
    
            }
        }
    
    
    }