<template>
    <div class="input-group mb-3">
        <input type="text" class="form-control" placeholder="Search by title or genre" @input="search" v-model="query">
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { defineEmits } from 'vue'

// Declare the reactive query state
const query = ref('')

// Define the emit function with custom events
const emit = defineEmits(['search'])

// Emit the search query to the parent component
const search = () => {
    emit('search', query.value)
}
</script>
