<template>
  <section>
    <h1>Diaries</h1>
    <ModelTable v-bind:model="{name: 'diary'}"/>
  </section>
</template>

<script>
import ModelTable from "@/components/ModelTable.vue";

export default {
  name: "Diary",
  components: {
    ModelTable,
  },
};
</script>
