
const app = Vue.createApp({
  data(){
    return {
      comments:[
        {
          username:"alice",
          content:"First comment!"
        },
        {
          username:"bob",
          content:"hello world!"
        },
        {
          username:"ironman",
          content:"new armor comming soon!"
        },
        {
          username:"superman",
          content:"kryptonite is bad!"
        }
      ]
    }
  }
});

app.component("comment", {
  props: {
    comment: {
      type: Object,
      required: true
    }
  },
  template:`
      <div>
        <div class="card-body">
          <strong><p>{{comment.username}}</p></strong>
          <p>{{comment.content}}</p>
        </div>
        <hr>
      </div>
  `
})

const mountedApp = app.mount("#app")