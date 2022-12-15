<script lang="ts" >
import axios from "axios"
import { defineComponent, onBeforeMount, onMounted, ref } from "vue"
import { store } from '../store/store'

export default defineComponent({

  data() {
    return {
      products: [],
      productName: "",
      productDescription:"",
      productPrice: ""
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
    },
    isAdmin() {
        if(store.state.role == "ADMIN") {
          return true;
        }
        return false;
    },
    createProduct() {
      console.log(this.productName)
      console.log(this.productPrice)
      console.log(this.productDescription)
      axios.post("/create_product", {
        "name": this.productName,
        "price": parseInt(this.productPrice),
        "description": this.productDescription
      })
      .then(this.getProducts)
    },
    showUpdateProductForm(id: number, name: string, description: string, price: number) {
      const cards = document.getElementsByClassName("card")
      const nameElement = document.getElementById("name" + id);
      const descriptionElement = document.getElementById("description" + id);
      const priceElement = document.getElementById("price" + id);
      const editButtonElement = document.getElementById("edit" + id);
      const deleteButtonElement = document.getElementById("delete" + id);
      if(nameElement && descriptionElement && priceElement && editButtonElement && deleteButtonElement) {
        nameElement.style.display = "none"
        descriptionElement.style.display = "none";
        priceElement.style.display = "none";
        editButtonElement.style.display = "none";
        deleteButtonElement.style.display = "none";
      }

      const form = document.getElementById("form" + id)
      if(form) {
        form.style.display = "flex"
        form.style.alignItems = "center";
        form.style.justifyContent = "center";
        form.style.flexDirection = "column"
      }
    },
    updateProduct(id: number) {
      axios.post("/update_product", {
        "id": id,
        "name": this.productName,
        "price": parseInt(this.productPrice),
        "description": this.productDescription
      })
      .then(this.getProducts)
    },
    deleteProduct(id: number) {
      axios.post("/delete_product", {
        "id": id
      })
      .then(this.getProducts)
    }
  },
  beforeMount() {
    this.getProducts()
  }
})  
</script>

<template>
  <div class="container">
    <div v-if="isAdmin()" class="card">
      <form id="form">
      <h1>Create Product</h1>
      <input v-model="productName" type="text" name="productName" class="box" placeholder="Name" required>
      <input v-model="productDescription" type="text" name="productDescription" class="box" placeholder="Description" required>
      <input v-model="productPrice" type="text" name="productPrice" class="box" placeholder="Price" required>
      <button class="btn" @click="createProduct()">Create product</button>
      </form>
    </div>
    <div class="card" v-for="product in products">
      <form :id="`form${product['id']}`" style="display: none;">
      <h1>Update Product</h1>
      <input v-model="productName" type="text" name="productName" class="box" placeholder="Name" required>
      <input v-model="productDescription" type="text" name="productDescription" class="box" placeholder="Description" required>
      <input v-model="productPrice" type="text" name="productPrice" class="box" placeholder="Price" required>
      <button class="btn" @click="updateProduct(product['id'])">Update product</button>
      </form>
      <h2 :id="`name${product['id']}`">{{product['name']}}</h2>
      <p :id="`description${product['id']}`">Description: {{product['description']}}</p>
      <p :id="`price${product['id']}`">{{product['price']}} USD</p>
      <button v-if="!isAdmin()" class="btn" @click="pay(product['name'], product['price'])">Buy</button>
      <button v-if="isAdmin()" :id="`edit${product['id']}`" class="btn" @click="showUpdateProductForm(product['id'], product['name'], product['description'], product['price'])">Edit</button>
      <button v-if="isAdmin()" :id="`delete${product['id']}`" class="btn" @click="deleteProduct(product['id'])">Delete</button>
    </div>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  flex-wrap: wrap;
}

.card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 30%;
  height: 40vh;
  background: #11101b;;
  border-radius: 10px;
  margin: 20px;
}

.btn {
  margin-bottom: 10px;
  width: 50%;
}

.btn:hover {
  cursor: pointer;
}

#form {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  background: #11101b;
}

.box {
  padding: 5px;
  width: 60%;
  margin: 15px;
}
</style>
