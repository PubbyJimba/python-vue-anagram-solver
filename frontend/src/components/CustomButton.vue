<template>
  <button @click="$emit('click-action')" :disabled="loading">
    {{ title }}
  </button>
</template>

<script setup>
defineProps({
  title: {
    type: String,
    required: true,
  },
  loading: {
    type: Boolean,
    required: false,
  },
  bgColor: {
    type: String,
    default: "#42b883",
  },
});

defineEmits(["click-action"]);
</script>

<style scoped>
button {
  padding: 0.5rem 1rem;
  font-size: 1.2rem;
  background-color: v-bind(bgColor);
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:disabled {
  background-color: #9c9c9c;
  cursor: not-allowed;
}
</style>
