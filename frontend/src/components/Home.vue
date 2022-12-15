<script lang="ts" >
import axios from "axios"
import { defineComponent, onBeforeMount, onMounted, ref } from "vue"

export default defineComponent({

  data() {
    return {
      products: [],
    }
  },
  methods: {
    getProducts() {
      axios("/get_products")
      .then(res => this.products = res.data.products)
      .catch(e => console.log(e))
    },
    pay(name: string, amount: number) {
      axios.post("/stripe-checkout", {
        "name": name,
        "amount": amount
      })
      .then(res => res.data)
      .then(data => {
        console.log(data)
        window.location = data.url
      })
    }
  },
  beforeMount() {
    this.getProducts()
  }
})  
</script>

<template>
  <div class="container">
    <div class="card" v-for="product in products">
        <h2 class="name">{{product['name']}}</h2>
        <p class="description">Description: {{product['description']}}</p>
        <p class="price">{{product['price']}} USD</p>
        <button class="buy-btn" @click="pay(product['name'], product['price'])">Buy</button>
    </div>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  width: 100vw;
  height: 90vh;
  overflow: hidden;
}

.card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 20vw;
  height: 30vh;
  background: #11101b;;
  border-radius: 10px;
  margin: 20px;
}

.buy-btn {
  width: 40%;
}

.buy-btn:hover {
  cursor: pointer;
}
</style>
