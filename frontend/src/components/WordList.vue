<template>
  <Transition name="fade" mode="out-in">
    <div v-if="words.length > 0" class="results">
      <h3>{{ title }}</h3>
      <ul>
        <li
          v-for="word in words"
          :key="word"
          @click="$emit('copy', word)"
          class="clickable-word"
          title="Click to copy"
        >
          {{ word }}
        </li>
      </ul>
    </div>
  </Transition>
</template>

<script setup>
defineProps({
  words: {
    type: Array,
    required: true,
  },
  title: {
    type: String,
    required: true,
  },
});

defineEmits(["copy"]);
</script>

<style scoped>
ul {
  list-style-type: none;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

li {
  background: #525169;
  padding: 0.3rem 0.8rem;
  border-radius: 4px;
  font-size: 1.1rem;
}

.results {
  text-align: left;
  background: #3b3b3b;
  padding: 1rem;
  margin: 8px;
  border: 1px solid #ccc;
  border-radius: 8px;
  color: #ffffff;
}

.clickable-word {
  cursor: pointer;
  transition: color 0.2s ease;
}

.clickable-word:hover {
  text-decoration: underline;
}

.clickable-word:active {
  transform: scale(0.95);
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
