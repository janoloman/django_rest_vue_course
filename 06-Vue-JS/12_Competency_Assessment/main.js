
const app = Vue.createApp({
  data(){
    return {
      tasks: [],
      error: null
    }
  },
  methods: {
    addNewTask(newTask) {
      this.tasks.push(newTask);
    }
  }
});

// task list component
app.component("task-list", {
  emits: ["submit-task", "remove-task"],
  props:{
    tasks: {
      type: Array,
      required: true
    }
  },
  data(){
    return {
      taskDescription: null,
      remainingTasks: 0,
      error: null
    }
  },
  methods: {
    onSubmit() {
      if(this.taskDescription){
        const newTask = {
          description: this.taskDescription,
          error: null
        };
        this.$emit("submit-task", newTask);
        this.remainingTasks = this.tasks.length;

        this.taskDescription = null;
        if(this.error) {
          this.error = null
        }

      } else {
        this.error="Please fill out the task description!"
      }
    },
    removeTask(task) {
      console.log("task-list removeTask:" + task);
      const index = this.tasks.indexOf(task);
      if (index !== -1) {
        this.tasks.splice(index, 1);
        this.remainingTasks = this.tasks.length;
      }
    }
  },
  template: `
    <div class="container mt-2">
      <h4 class="col-12">Remaining Tasks: {{remainingTasks}}</h4>
      <p>{{error}}</p>

      <form @submit.prevent="onSubmit">
        <div class="form-group">
          <input v-model="taskDescription"
            type="text"
            class="form-control"
            id="taskDescription"
            placeholder="What do you need to do?">
        </div>
      </form>

      <p v-if="remainingTasks == 0">To add a new task, write something and press enter!</p>
      <single-task v-for="(task, index) in tasks"
        :task="task"
        :key="index"
        @remove-task="removeTask"
        >
      </single-task>
    </div>
  `
})


// single task component
app.component("single-task", {
  props: {
    task: {
      type: Object,
      required: true
    }
  },
  methods: {
    removeTask() {
      console.log("single-task removeTask: "+ this.task);
      this.$emit("remove-task", this.task);
    }
  },
  template:`
  <div class="col-12 mt-2">
    <div class="alert alert-success alert-dismissible fade show" role="alert">
      {{task.description}}
      <button
        @click="removeTask"
        type="button"
        class="custom-close btn-close"
        aria-label="Close">
      </button>
    </div>
  </div>
  `
})

const mountedApp = app.mount("#app")