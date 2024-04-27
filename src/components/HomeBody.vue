<template> 
<section class="homebody">
    <div class="homeimg">
        <img src="../assets/home1.png" alt="">
    </div>
    <div class="homecontent">
        <div class="head">
          <img class="headicon" src="../assets/camera.png" alt="">
          <span>
            Photogram
          </span>
        </div>
        <p> 
          Share Photos of your favourite momemts with friends, family and the world.
        </p>
        <div class="buttencombo">
            <RouterLink to="/register" class="register">Register</RouterLink>
            <RouterLink to="/login" class="login">Login</RouterLink>
        </div>
    </div>
</section>

</template>
<script> 
//import { ref, onMounted } from "vue"; 
//let csrf_token = ref(""); 
export default{
    data(){
        return{
            message:'',
            csrf_token:"",
        }
    },
    methods:{
        
    },
    created(){
       
    },
}

</script>
<style>
section.homebody{
    display: grid;
    grid-template-columns: repeat(2,1fr);
    grid-gap: 1em;
    padding: 4em;
    position: absolute;
    top: 50%;
    right: 50%;
    transform: translate(50%, -50%);
    width: 80%;
}
div.homeimg,div.homecontent{
    box-shadow: rgba(0, 0, 0, 0.16) 0px 3px 6px, rgba(0, 0, 0, 0.23) 0px 3px 6px;
}
 div.homeimg img{
    width: 30rem;
 }
 div.homecontent{
    display: flex;
    flex-flow: column;
    padding: 1.5em 1em ;
 }
 img.headicon{
    width: 1.5em;
    height: 1.5em;
    align-self: center;
    margin-right: 0.5em;
 }
 div.head{
    display: flex;
    flex-flow: row nowrap;
    justify-content: center;
    border-bottom: solid #999 0.07em;
    margin-bottom: 1em;
 }
 div.buttencombo{
    display: grid;
    grid-template-columns: repeat(2,1fr);
    grid-gap: 1.5em;
 }
 a.login,a.register{
    padding: 0.75em;
    text-decoration: none;
    text-align: center;
    color: #fff;
 }
 a.register{
    background: #5cb85c;
 }
 a.login{
    background: #6495ed;
 }
 div.homecontent p{
    margin-bottom: 4em;
 }
</style>