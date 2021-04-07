<template>
  <nav class="text-center">
    <router-link to="/" class="text-green-500 hover:text-green-400">Home</router-link>
    <span class="text-green-600"> | </span>
    <router-link to="/diary" class="text-green-500 hover:text-green-400">Diary</router-link>
  </nav>
  <router-view/>
</template>

<style>
@import './assets/tailwind.css';
@import './assets/css/base.css';
</style>