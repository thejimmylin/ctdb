<template>
  <section class="container max-w-full justify-center">
    <h1 class="text-green-900">{{ tableTitle }}</h1>
    <ModelTable :fields="fields" />
  </section>
</template>

<script>
import ModelTable from "@/components/ModelTable.vue";
import axios from 'axios';

export default {
  name: "Diary",
  components: {
    ModelTable,
  },
  data() {
    return {
      tableTitle: "News",
      fields: [
        {name: "id", verboseName: "ID"},
        {name: "date", verboseName: "Date"},
        {name: "daily_check", verboseName: "Daily check"},
        {name: "daily_record", verboseName: "Daily record"},
        {name: "todo", verboseName: "TODO"},
        {name: "remark", verboseName: "Remark"},
        {name: "created_by", verboseName: "Created by"},
      ],
      results: []
    }
  },
  methods: {
    getResults() {
      axios.get('http://localhost:8000/api/diaries/')
      .then(response => {this.results = response.data;})
      .then(console.log);
    }
  },
  created() {
    this.getResults();
  },
};
</script>
