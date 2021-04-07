<template>
  <nav class="text-center">
    <router-link to="/news" class="text-green-500 hover:text-green-400">News</router-link>
    <span class="text-green-600"> | </span>
    <router-link to="/diaries" class="text-green-500 hover:text-green-400">Diary</router-link>
  </nav>
  <router-view/>
</template>

<style>
@import './assets/tailwind.css';
@import './assets/css/base.css';
</style>