<script lang="ts">
import Navbar from './components/Navbar.vue'
import { store } from './store/store'
import { defineComponent } from "vue"
import axios from "axios"

export default defineComponent({
  components: {
    Navbar
  },
  beforeMount() {
    axios.post("/authenticate")
    .then(res => res.data)
    .then(data => {
      store.state.is_authenticated = data.is_authenticated
      if(data.role) {
        store.state.role = data.role
      }
    })
  }
})
</script>

<template>
  <Navbar/>

  <router-view></router-view>
</template>

<style scoped>
</style>
