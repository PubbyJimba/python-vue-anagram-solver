<script setup>
import { computed, ref } from "vue";
import WordList from "./components/WordList.vue";
import CustomButton from "./components/CustomButton.vue";

const letters = ref("");
const anagrams = ref([]);
const twos = ref([]);
const threes = ref([]);
const fours = ref([]);
const fives = ref([]);
const sixes = ref([]);
const sevens = ref([]);
const error = ref("");
const loading = ref(false);

const solve = async () => {
  if (!letters.value.trim()) {
    error.value = "Please enter some letters";
    return;
  }

  error.value = "";
  loading.value = true;
  [anagrams, twos, threes, fours, fives, sixes, sevens].forEach((r) => {
    r.value = [];
  });

  try {
    const [response] = await Promise.all([
      fetch(`http://127.0.0.1:8000/solve/${letters.value.trim()}`),
      new Promise((resolve) => setTimeout(resolve, 500)), // 500ms minimum delay
    ]);

    if (!response.ok) {
      const data = await response.json();
      throw new Error(data.detail || "Failed to solve");
    }

    const data = await response.json();
    anagrams.value = data.anagrams;

    if (anagrams.value.length === 0) {
      error.value = "No anagrams found";
    }

    for (let i = 0; i < anagrams.value.length; i++) {
      const word = anagrams.value[i];
      switch (word.length) {
        case 2:
          twos.value.push(word);
          break;
        case 3:
          threes.value.push(word);
          break;
        case 4:
          fours.value.push(word);
          break;
        case 5:
          fives.value.push(word);
          break;
        case 6:
          sixes.value.push(word);
          break;
        case 7:
          sevens.value.push(word);
          break;
      }
    }
  } catch (e) {
    error.value = e.message;
  } finally {
    loading.value = false;
  }
};

const reset = async () => {
  letters.value = "";
  error.value = "";
  loading.value = false;
  [anagrams, twos, threes, fours, fives, sixes, sevens].forEach((r) => {
    r.value = [];
  });
};

const copyToClipboard = async (word) => {
  try {
    await navigator.clipboard.writeText(word);
  } catch (err) {
    error.value = "Failed to copy text";
  }
};

const wordConfigs = computed(() => [
  { title: "Two letter words:", data: twos.value },
  { title: "Three letter words:", data: threes.value },
  { title: "Four letter words:", data: fours.value },
  { title: "Five letter words:", data: fives.value },
  { title: "Six letter words:", data: sixes.value },
  { title: "Seven letter words:", data: sevens.value },
]);
</script>

<template>
  <div class="container">
    <h1>Anagram Solver</h1>

    <div class="input-group">
      <input
        v-model="letters"
        @keyup.enter="solve"
        placeholder="Enter letters (e.g., 'eat')"
        maxlength="7"
      />
      <CustomButton
        :title="loading ? 'Solving...' : 'Solve'"
        :loading="loading"
        @click-action="solve"
      />
      <CustomButton title="Reset" bg-color="#b84242" @click-action="reset" />
    </div>

    <div v-if="error" class="error">
      {{ error }}
    </div>
    <WordList
      v-for="list in wordConfigs"
      :key="list.title"
      :title="list.title"
      :words="list.data"
      @copy="copyToClipboard"
    />
  </div>
</template>

<style scoped>
.container {
  max-width: 600px;
  margin: 0 auto;
  padding: 2rem;
  text-align: center;
  font-family: Arial, sans-serif;
}

.input-group {
  display: flex;
  gap: 0.5rem;
  justify-content: center;
  margin-bottom: 2rem;
}

input {
  padding: 0.5rem;
  font-size: 1.2rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 250px;
}

.error {
  color: #e74c3c;
  margin-bottom: 1rem;
}
</style>
