<script lang="ts">
  import axios from "axios"
  import { defineComponent } from "vue";
  export default defineComponent({
    data() {
      return {
        username: "",
        password: ""
      }
    },
    methods: {
      register() {
        axios.post("/register", {
          username: this.username,
          password: this.password
        })
        .then(res => console.log(res))
        .catch(e => console.log(e))
      }
    }
  })
</script>

<template>
  <div class="container">
    <form id="form">
      <h1>Register</h1>
      <input v-model="username" type="text" name="username" class="box" placeholder="Enter username" required>
      <input v-model="password" type="password" name="password" class="box" placeholder="Enter password" required>
      <button type="button" class="submit" @click="register">Register</button>
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
