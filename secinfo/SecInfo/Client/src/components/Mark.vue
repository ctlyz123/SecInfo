<template>
  <el-collapse  v-model="activeNames" @change="handleChange">
    <template v-for="(value,hash,index) in sites" >
      <el-collapse-item :title="value.time" :key="hash" ref="hash">
      <div>{{value.content}}</div>
      <el-button @click="handledeletemark(hash)" type="danger" icon="el-icon-delete" circle></el-button>
      </el-collapse-item>
    </template>
  </el-collapse>
</template>
<script>

// import axios from 'axios'
import qs from 'qs'

export default {
  name: 'Unread',
  data () {
    return {
      activeNames: ['1'],
      sites: {}
    }
  },
  watch:{
  tab:function(){
    this.mounted(() => { });
  },

},
  mounted () {
    this.handleshowmark(1)
  },
  methods: {
    handleChange () {
      console.log('abc')
    },
    handledeletemark (hash) {

        this.$ajax.post("/delete",qs.stringify({hash:hash,mark:1})).then((response) => {
            if (response.data != "error") {
              console.log(response.data)
                this.sites = response.data
            }
          }).catch((response) => {
            this.$Message.error({
              content: '查询出错！' + response,
            });
          })

    },

    handleshowmark (mark) {
      this.$ajax.post("/show",qs.stringify({mark:mark})).then((response) => {
          if (response.data != "error") {
            // console.log(response.data)

          this.sites = response.data

          }
        }).catch((response) => {
          this.$Message.error({
            content: '查询出错！' + response,
            duration: 3,
          });
        })
    }
  }
}
</script>
