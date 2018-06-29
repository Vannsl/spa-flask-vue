<template>
  <div class="faq page">
    <h1>This is the FAQ page</h1>
    <div
      v-for="faq in faqList"
      :key="faq.id"
    >
      <h2>{{faq.title}}</h2>
      <p>{{faq.message}}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Faq',
  data() {
    return {
      faqList: [],
    };
  },
  methods: {
    getFaqList() {
      axios.get('http://localhost:5000/api/faq')
        .then((response) => {
          this.faqList = response.data;
        })
        .catch(error => console.log(error));
    },
  },
  created() {
    this.getFaqList();
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  font-weight: normal;
}
</style>
