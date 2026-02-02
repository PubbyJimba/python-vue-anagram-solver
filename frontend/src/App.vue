<script setup>
import { ref } from "vue";

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
    const response = await fetch(
      `http://127.0.0.1:8000/solve/${letters.value.trim()}`
    );
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
      <button @click="solve" :disabled="loading">
        {{ loading ? "Solving..." : "Solve" }}
      </button>
      <button @click="reset" class="reset-button">Reset</button>
    </div>

    <div v-if="error" class="error">
      {{ error }}
    </div>
    <div v-if="twos.length > 0" class="results">
      <h3>Two letter words:</h3>
      <ul>
        <li
          v-for="word in twos"
          :key="word"
          @click="copyToClipboard(word)"
          class="clickable-word"
          title="Click to copy"
        >
          {{ word }}
        </li>
      </ul>
    </div>
    <div v-if="threes.length > 0" class="results">
      <h3>Three letter words:</h3>
      <ul>
        <li
          v-for="word in threes"
          :key="word"
          @click="copyToClipboard(word)"
          class="clickable-word"
          title="Click to copy"
        >
          {{ word }}
        </li>
      </ul>
    </div>
    <div v-if="fours.length > 0" class="results">
      <h3>Four letter words:</h3>
      <ul>
        <li
          v-for="word in fours"
          :key="word"
          @click="copyToClipboard(word)"
          class="clickable-word"
          title="Click to copy"
        >
          {{ word }}
        </li>
      </ul>
    </div>
    <div v-if="fives.length > 0" class="results">
      <h3>Five letter words:</h3>
      <ul>
        <li
          v-for="word in fives"
          :key="word"
          @click="copyToClipboard(word)"
          class="clickable-word"
          title="Click to copy"
        >
          {{ word }}
        </li>
      </ul>
    </div>
    <div v-if="sixes.length > 0" class="results">
      <h3>Six letter words:</h3>
      <ul>
        <li
          v-for="word in sixes"
          :key="word"
          @click="copyToClipboard(word)"
          class="clickable-word"
          title="Click to copy"
        >
          {{ word }}
        </li>
      </ul>
    </div>
    <div v-if="sevens.length > 0" class="results">
      <h3>Seven letter words:</h3>
      <ul>
        <li
          v-for="word in sevens"
          :key="word"
          @click="copyToClipboard(word)"
          class="clickable-word"
          title="Click to copy"
        >
          {{ word }}
        </li>
      </ul>
    </div>
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

button {
  padding: 0.5rem 1rem;
  font-size: 1.2rem;
  background-color: #42b883;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.reset-button {
  padding: 0.5rem 1rem;
  font-size: 1.2rem;
  background-color: #b84242;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.error {
  color: #e74c3c;
  margin-bottom: 1rem;
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
</style>
