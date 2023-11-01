<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>
      <a href="https://github.com/xyjigsaw/FullStackDemo" target="_blank">Github</a>
      <a href="https://omegaxyz.com" target="_blank">Website</a>
    </h2>
    <el-input-number v-model="num" :min="1" :max="100" label="Number of papers"></el-input-number>
    <el-button icon="el-icon-search" @click="fetch_paper(num)">Search</el-button>
    <div style="padding: 10px 200px 10px 200px">
      <!-- table -->
      <el-table :data="tableData" style="width: 100%" stripe>
        <el-table-column prop="title" label="Title"></el-table-column>
        <el-table-column prop="date" label="Date" width="150"></el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'FullStack Demo',
      tableData: [],
      num: 10,
    }
  },

  methods: {
    fetch_paper(num) {
      const limit=num
      const param = `num=${limit}`;
      // 在这里调接口
      axios
        .get(`http://127.0.0.1:8000/paper?${param}`)
        .then((res) => {
          this.tableData = res.data.data;
          this.time = res.data.time;
          console.log(this.tableData, this.time);
        })
        .catch(() => {
          this.$notify({
            title: "Error",
            message: "Please try again!",
            type: "error",
          });
        });

    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
a {
  color: #42b983;
}
</style>
