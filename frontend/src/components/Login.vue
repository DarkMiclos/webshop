<script lang="ts">
  import axios from "axios"
  import { defineComponent } from "vue";
  import { useStore, store } from '../store/store'
  export default defineComponent({
    data() {
      return {
        username: "",
        password: ""
      }
    },
    methods: {
      login() {
        axios.post("/login", {
          username: this.username,
          password: this.password,
        },
        {
          headers: {},
        })
        .then(res => {
          store.state.is_authenticated = res.data.is_authenticated
          store.state.role = res.data.role
          console.log(store.state.is_authenticated)
          console.log(store.state.role)
        })
        .catch(e => console.log(e))
      }
    }
  })
</script>

<template>
  <div class="container">
    <form id="form">
      <h1>Login</h1>
      <input v-model="username" type="text" name="username" class="box" placeholder="Enter username" required>
      <input v-model="password" type="password" name="password" class="box" placeholder="Enter password" required>
      <button type="button" class="submit" @click="login">Login</button>
      </form>
  </div>
</template>

<style scoped>
.container {
  margin-top: 20vh;
  display: flex;
  justify-content: center;
  margin-bottom: 20vh;
}

#form {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  height: 50vh;
  width: 50vw;
  background: #11101b;
  border-radius: 20px;
}

#form h1 {
  margin: 15px;
}

.box {
  padding: 10px;
  width: 60%;
  margin: 15px;
}

.submit {
  padding: 10px 25px;
  margin-top: 50px;
  width: 40%;
}
</style>
