
const app = Vue.createApp({
  data() {
    return {
      users: [
        {
          id: 567,
          name: "alice",
          profession: "developer"
        },
        {
          id: 568,
          name: "bob",
          profession: "manager"
        },
        {
          id: 569,
          name: "charlie",
          profession: "cleaner"
        },
        {
          id: 570,
          name: "david",
          profession: "CEO"
        },
        {
          id: 571,
          name: "eve",
          profession: "developer"
        },
        {
          id: 572,
          name: "frank",
          profession: "developer"
        }
      ]
    };
  },
})

const mountedApp = app.mount("#app")