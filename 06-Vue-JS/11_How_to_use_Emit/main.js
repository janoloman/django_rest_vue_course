
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
  },
  methods: {
    addNewComment(newComment) {
      this.comments.push(newComment);
    }
  }
});


// comment list component
app.component("comment-list", {
  emits: ["submit-comment"],
  props:{
    comments: {
      type: Array,
      required: true
    }
  },
  data(){
    return{
      commentAuthor: null,
      commentBody: null,
      error: null
    }
  },
  methods: {
    onSubmit() {
      if(this.commentAuthor && this.commentBody){
        const newComment = {
          username: this.commentAuthor,
          content: this.commentBody,
          error: null
        };
        this.$emit("submit-comment", newComment);

        this.commentAuthor = null;
        this.commentBody = null;

        if(this.error) {
          this.error = null
        }

      } else {
        this.error="Please fill out both fields!"
      }
    }
  },
  template: `
    <div class="container mt-2">
      <single-comment v-for="(comment, index) in comments"
        :comment="comment"
        :key="index"
        >
      </single-comment>
      <hr>
      <h3>{{error}}</h3>

      <form @submit.prevent="onSubmit">
        <div class="form-group">
          <label for="commentAuthor">Your Username</label>
          <input v-model="commentAuthor"
            type="text"
            class="form-control"
            id="commentAuthor">
        </div>
        <div class="form-group">
          <label for="commentBody">Add a comment!</label>
          <textarea v-model="commentBody"
            rows="3" cols="40"
            class="form-control"
            id="commentBody"></textarea>
        </div>
        <button class="btn btn-sm btn-primary" type="submit">Publish Comment</button>
      </form>
    </div>
  `
})


// single comment component
app.component("single-comment", {
  props: {
    comment: {
      type: Object,
      required: true
    }
  },
  template:`
  <div class="mb-2">
    <div class="card">
      <div class="card-header">
        <p>Published by: {{comment.username}}</p>
      </div>
      <div class="card-body">
        <p>{{comment.content}}</p>
      </div>
    </div>
  </div>
  `
})

const mountedApp = app.mount("#app")