<template>
  <div class="home">
    <h1>Homepage!</h1>
    <button @click="getQuestions">LOAD QUESTIONS</button>

    <div v-if="this.questions">
      {{ this.questions }}
    </div>
  </div>
</template>

<script>
import { axios } from "@/common/api.service.js";
export default {
  name: 'HomeView',
  data() {
    return {
      questions : []
    }
  },
  methods: {
    async getQuestions() {
      let endpoint = "/api/v1/questions/";
      try {
        const response = await axios.get(endpoint);
        this.questions = response.data
        console.log(this.questions);
      } catch (error) {
        console.log(error.response);
        alert(error.response.statusText);
      }
    }
  }
}
</script>
