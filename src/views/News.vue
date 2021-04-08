<template>
  <section class="container max-w-full justify-center">
    <h1 class="text-green-900">{{ tableTitle }}</h1>
    <ModelTable :fields="fields" :results="results"/>
  </section>
</template>

<script>
import ModelTable from "@/components/ModelTable.vue";
import axios from 'axios';

export default {
  name: "News",
  components: {
    ModelTable,
  },
  data() {
    return {
      tableTitle: "News",
      fields: [
        {name: "id", verboseName: "ID"},
        {name: "title", verboseName: "Title"},
        {name: "content", verboseName: "Content"},
        {name: "at", verboseName: "At"},
        {name: "created_by", verboseName: "Created by"},
      ],
      results: [],
    }
  },
  methods: {
    getResults() {
      axios.get('http://localhost:8000/api/news/')
      .then(response => {this.results = response.data;})
    }
  },
  created() {
    this.getResults();
  },
};
</script>
