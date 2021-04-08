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
        {name: "id", verboseName: "ID", isDisplayed: false},
        {name: "title", verboseName: "Title", isDisplayed: true},
        {name: "content", verboseName: "Content", isDisplayed: true},
        {name: "at", verboseName: "At", isDisplayed: true},
        {name: "created_by", verboseName: "Created by", isDisplayed: false},
      ],
      endpoint: "",
      results: [],
    }
  },
  methods: {
    getEndpoint() {
      this.endpoint = window.location.protocol + "//" + window.location.hostname + ":8000" + "/api/news/";
    },
    getResults() {
      axios.get(this.endpoint)
      .then(response => {this.results = response.data;})
    }
  },
  created() {
    this.getEndpoint();
    this.getResults();
  },
};
</script>
