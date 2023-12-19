
const app = Vue.createApp({
  data() {
    return {
      // auth: false
      product: "sunglasses",
      quantity: 150,
      sale: true
    };
  },
})

const mountedApp = app.mount("#app")