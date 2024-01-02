<template>
  <div>
    <p class="text-muted">
      <strong>{{ answer.author }} &#8901; {{ answer.created_at }}</strong>
    </p>
    <p style="white-space: pre-wrap">{{ answer.body }}</p>
    <div v-show="isAnswerAuthor">
      <router-link :to="{ name: 'answer-editor', params: { uuid: answer.uuid } }" class="btn btn-sm btn-warning me-1">
        Edit
      </router-link>
      <button class="btn btn-sm btn-danger mx-1" @click="showDeleteConfirmation = !showDeleteConfirmation">
        Delete
      </button>
      <button v-show="showDeleteConfirmation" class="btn btn-sm btn-outline-danger" @click="triggerDeleteAnswer">
        Yes, delete my answer!
      </button>
    </div>
    <hr />
  </div>
</template>

<script>
export default {
  name: "AnswerComponent",
  props: {
    answer: {
      type: Object,
      required: true,
    },
    requestUser: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      showDeleteConfirmation: false
    }
  },
  computed: {
    isAnswerAuthor() {
      return this.answer.author === this.requestUser;
    },
  },
  methods: {
    triggerDeleteAnswer() {
      this.$emit("delete-answer", this.answer);
    }
  }
};
</script>

<style></style>