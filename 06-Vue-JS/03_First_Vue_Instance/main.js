
const app = Vue.createApp({
  data() {
    return {
      message: "Hello world!",
      num: 5,
      img: "https://media.istockphoto.com/id/937170838/vector/television-test-pattern-of-stripes.jpg?s=612x612&w=0&k=20&c=wgalOobYWVpx8E0ynQNkMNNYNymLzuw-bu8uncvOIMM=",
      link: "https://www.vuejs.org/"
    };
  }
})

const mountedApp = app.mount("#app")