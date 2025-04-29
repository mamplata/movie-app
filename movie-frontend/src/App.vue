<template>
  <div id="app" class="container">
    <h1 class="my-4 text-center">🎬 My Movie Collection</h1>

    <!-- Add Movie Button -->
    <div class="d-flex justify-content-end mb-3">
      <button class="btn btn-success" @click="openModal()">Add Movie</button>
    </div>

    <!-- Search Bar -->
    <SearchBar @search="handleSearch" />

    <!-- Movie List -->
    <MovieList :movies="filteredMovies" @edit="startEdit" @delete="deleteMovie" />

    <!-- Modal -->
    <div class="modal fade" :class="{ show: showModal }" tabindex="-1" role="dialog"
      :style="{ display: showModal ? 'block' : 'none' }" aria-modal="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">{{ isEditing ? 'Edit Movie' : 'Add Movie' }}</h5>
            <button type="button" class="btn-close" @click="closeModal()" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <MovieForm :form="form" :is-editing="isEditing" :errors="formErrors" @submit="onModalSubmit"
              @reset="onModalReset" />
          </div>
        </div>
      </div>
    </div>
    <div class="modal-backdrop fade" :class="{ show: showModal }" v-if="showModal"></div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'
import MovieList from './components/MovieList.vue'
import MovieForm from './components/MovieForm.vue'
import SearchBar from './components/SearchBar.vue'

// Reactive state
const movies = ref([])
const form = ref({ title: '', genre: '', director: '', release_year: '', rating: '', poster: null })
const formErrors = ref({})
const searchQuery = ref('')
const editId = ref(null)
const showModal = ref(false)

// Computed
const filteredMovies = computed(() => {
  if (!searchQuery.value) return movies.value
  const q = searchQuery.value.toLowerCase()
  return movies.value.filter(m => m.title.toLowerCase().includes(q) || m.genre.toLowerCase().includes(q))
})
const isEditing = computed(() => editId.value !== null)

// API
const fetchMovies = () => {
  axios.get('http://localhost:8000/api/movies/')
    .then(res => { movies.value = res.data })
    .catch(console.error)
}

// Handlers
const handleSearch = q => (searchQuery.value = q)
const openModal = () => { resetForm(); showModal.value = true }
const startEdit = movie => { form.value = { ...movie }; editId.value = movie.id; showModal.value = true }
const closeModal = () => (showModal.value = false)
const resetForm = () => {
  form.value = { title: '', genre: '', director: '', release_year: '', rating: '', poster: null }
  formErrors.value = {}
  editId.value = null
}

// Submit: poster optional on edit or add
const onModalSubmit = updatedForm => {
  formErrors.value = {}

  if (updatedForm.rating < 1 || updatedForm.rating > 10) {
    formErrors.value.rating = ['Rating must be between 1 and 10.']
    return
  }

  const data = new FormData()
  Object.entries(updatedForm).forEach(([k, v]) => {
    if (k === 'poster') {
      if (v instanceof File) data.append(k, v)
    } else {
      data.append(k, v)
    }
  })

  const req = editId.value
    ? axios.put(`http://localhost:8000/api/movies/${editId.value}/`, data)
    : axios.post('http://localhost:8000/api/movies/', data)

  req
    .then(() => {
      fetchMovies()
      closeModal()
      resetForm()
    })
    .catch(err => {
      if (err.response && err.response.status === 400) {
        formErrors.value = err.response.data
      } else {
        console.error(err)
      }
    })
}

const onModalReset = () => { closeModal(); resetForm() }
const deleteMovie = id => axios.delete(`http://localhost:8000/api/movies/${id}/`).then(fetchMovies).catch(console.error)

onMounted(fetchMovies)
</script>

<style>
/* Optional minimal styling */
</style>