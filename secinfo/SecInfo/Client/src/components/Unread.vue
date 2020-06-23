<template>
  <el-collapse  v-model="activeNames" @change="handleChange">
    <template v-for="(value,hash,index) in sites" >
      <el-collapse-item :title="value.time" :key="hash" ref="hash">
      <div>{{value.content}}</div>
      <el-button @click="handledelete(hash)" type="danger" icon="el-icon-delete" circle></el-button>
      <el-button @click="handleaddmark(hash)" type="warning" icon="el-icon-star-off" circle></el-button>
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
    watch: {
    // 监听json数据变化，重新渲染文件夹内容
    sites(newVal) {
        this.file_is_show = false
        if (true) {
            this.$nextTick(()=>{ // $nextTick 是在 DOM 更新循环结束之后执行延迟回调
                this.file_is_show = true
            })
        }
    }
},
  mounted () {
    this.handleshow()
  },
  methods: {

    handleChange () {
    },
    handledelete (hash) {
        this.$ajax.post("/delete",qs.stringify({hash:hash})).then((response) => {
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
    handleaddmark (hash) {
        this.$ajax.post("/addmark",qs.stringify({hash:hash})).then((response) => {
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
    handleshow () {
      this.$ajax.get("/show").then((response) => {
          if (response.data != "error") {
            console.log(response.data)
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
