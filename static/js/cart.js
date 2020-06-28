console.log("linked")
var btn=document.getElementsByClassName('carts')

for( i=0;i<btn.length;i++){
    btn[i].addEventListener('click',function(){
        var p_id=this.dataset.product
        var a=this.dataset.action
        console.log('id:',p_id ,'a:',a)
  
        
    })
}


function update_cart(id,a){
    var url='update_cart/'
    fetch(url,{
        method:'POST',
        header:{
            'Content-Type':'application/json'
        },
        body:
            JSON.stringify({'Product_id':id,'Action':'a'})
        
    })
    .then((reponse)=>{return response.json()})

    .then( (data)=>{'data:',data})

}
