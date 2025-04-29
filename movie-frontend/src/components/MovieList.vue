<template>
    <div class="d-flex flex-wrap gap-3 mt-3">
        <MovieCard v-for="movie in movies" :key="movie.id" :movie="movie" @edit="$emit('edit', movie)"
            @delete="$emit('delete', movie.id)" />
    </div>
</template>

<script setup>
import { defineProps } from 'vue'
import MovieCard from './MovieCard.vue'

// Directly define the 'movies' prop
defineProps({
    movies: {
        type: Array,
        required: true
    }
})
</script>

<style scoped>
/* Optional minimal styling */
</style>
