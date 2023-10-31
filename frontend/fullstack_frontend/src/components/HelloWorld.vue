<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>Essential Links</h2>
    <h2>Ecosystem</h2>
    <el-button icon="el-icon-search" @click="fetch_paper"></el-button>
    <!-- table -->
    <el-table :data="tableData" style="width: 100%">
      <el-table-column prop="title" label="Title"></el-table-column>
    </el-table>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      tableData: [],
    }
  },

  methods: {
    fetch_paper() {
      const limit=8
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
