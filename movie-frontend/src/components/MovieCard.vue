<template>
    <div class="card" style="width: 18rem;">
        <img :src="movie.poster" class="card-img-top" alt="Poster">
        <div class="card-body">
            <h5 class="card-title">{{ movie.title }}</h5>
            <p class="card-text">
                Genre: {{ movie.genre }}<br>
                Director: {{ movie.director }}<br>
                Year: {{ movie.release_year }}<br>
                Rating: {{ movie.rating }}
            </p>
            <button class="btn btn-primary" @click="$emit('edit', movie)">Edit</button>
            <button class="btn btn-danger" @click="$emit('delete', movie.id)">Delete</button>
        </div>
    </div>
</template>

<script setup>
import { defineProps } from 'vue'
defineProps({
    movie: {
        type: Object,
        required: true
    }
})
</script>
