<script lang="ts">
  import axios from "axios"
  import { defineComponent } from "vue";
  import { key, store } from '../store/store'
  export default defineComponent({
    methods: {
      logout() {
        axios.post("/logout")
        .then(res => {
          store.state.is_authenticated = res.data.is_authenticated
          console.log(store.state.is_authenticated)
        })
        .catch(e => console.log(e))
      },
      setActive() {
        let navbar = document.getElementById("nav-bar");
        navbar?.classList.toggle("active");
      },
      isAuthenticated() {
        return store.state.is_authenticated;
      }
    }
  })
</script>

<template>
  <header>
    <router-link to="/" id="logo">Webshop</router-link>
    <div id="hamburger" @click="setActive">
      <div class="line"></div>
      <div class="line"></div>
      <div class="line"></div>
    </div>
    <nav id="nav-bar">
      <ul>
        <li>
          <router-link to="/" class="active">Home</router-link>
        </li>
        <li>
          <router-link to="/about" >About</router-link>
        </li>
        <li>
          <router-link to="/login" v-if="isAuthenticated() === false">Login</router-link>
        </li>
        <li>
          <router-link to="/register" v-if="isAuthenticated() === false">Register</router-link>
        </li>
        <li>
          <router-link to="/" @click="logout" v-if="isAuthenticated() === true">Logout</router-link>
        </li>
      </ul>
    </nav>
  </header>
</template>

<style scoped>
header {
  height: 10vh;
  background: #11101b;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 100px;
}

#logo {
  font-size: 28px;
  font-weight: bold;
  color: #fefefe;
}

#hamburger {
  display: none;
}

#nav-bar ul {
  display: flex;
}

#nav-bar ul li a {
  display: block;
  color: #fefefe;
  font-size: 20px;
  padding: 10px 25px;
  border-radius: 50px;
  transition: 0.2s;
  margin: 0 5px;
}

#nav-bar ul li a:hover {
  color:#11101b;
  background: #fefefe;
}

#nav-bar ul li a.active{
  color:#11101b;
  background: #fefefe;
}

@media only screen and (max-width: 1320px) {
  header {
    padding: 0 50px;
  }
}

@media only screen and (max-width: 1100px) {
  header {
    padding: 0 30px;
  }
}

@media only screen and (max-width: 900px) {
  #hamburger {
    display: block;
    cursor: pointer;
  }

  #hamburger .line {
    width: 30px;
    height: 3px;
    background: #fefefe;
    margin: 6px 0;
  }

  #nav-bar {
    height: 450px;
    position: absolute;
    top: 10vh;
    left: 0;
    right: 0;
    width: 100vw;
    background: #11101b;
    transition: 0.2s;
    opacity: 0;
  }

  #nav-bar.active{
    height: 450px;
    opacity: 1;
  }

  #nav-bar ul {
    display: block;
    width: fit-content;
    margin: 80px auto 0 auto;
    text-align: center;
    transition: 0.5s;
  }

  #nav-bar ul li a {
    margin-bottom: 12px;
  }
}
</style>
