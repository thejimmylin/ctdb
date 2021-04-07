<template>
  <section>
    <h1>News</h1>
    <Table v-bind="{name: 'news'}"/>
  </section>
</template>

<script>
// @ is an alias to /src
import Table from "@/components/Table.vue";

export default {
  name: "News",
  components: {
    Table,
  },
};
</script>
