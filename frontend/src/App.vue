<script setup>
import { ref } from 'vue'

const letters = ref('')
const anagrams = ref([])
const error = ref('')
const loading = ref(false)

const solve = async () => {
  if (!letters.value.trim()) {
    error.value = 'Please enter some letters'
    return
  }
  
  error.value = ''
  loading.value = true
  anagrams.value = []

  try {
    const response = await fetch(`http://127.0.0.1:8000/solve/${letters.value.trim()}`)
    if (!response.ok) {
      const data = await response.json()
      throw new Error(data.detail || 'Failed to solve')
    }
    const data = await response.json()
    anagrams.value = data.anagrams
    if (anagrams.value.length === 0) {
      error.value = 'No anagrams found'
    }
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
}
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
        {{ loading ? 'Solving...' : 'Solve' }}
      </button>
    </div>

    <div v-if="error" class="error">
      {{ error }}
    </div>

    <div v-if="anagrams.length > 0" class="results">
      <h2>Results:</h2>
      <ul>
        <li v-for="word in anagrams" :key="word">{{ word }}</li>
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
  background: #f9f9f9;
  padding: 1rem;
  border-radius: 8px;
  color: #2c3e50;
}

ul {
  list-style-type: none;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

li {
  background: #eee;
  padding: 0.3rem 0.8rem;
  border-radius: 4px;
  font-size: 1.1rem;
}
</style>