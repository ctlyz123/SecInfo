<template>
  <el-collapse  v-model="activeNames" @change="handleChange">
    <template v-for="(value,hash,index) in sites" >
      <el-collapse-item :title="value.time" :key="hash" ref="hash">
      <div>{{value.content}}</div>
      <el-button @click="handledelete(hash)" type="danger" icon="el-icon-delete" circle></el-button>
      </el-collapse-item>
    </template>
  </el-collapse>
</template>
<script>

import axios from 'axios'
import qs from 'qs'

export default {
  name: 'HelloWorld',
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
      console.log('abc')
      // this.sites = [{ name: '1' }, { name: '2' }, { name: 's' }]
    },
    handledelete (hash) {
        // delete this.sites[hash]
        // var test = this.sites
        axios.post("http://127.0.0.1:9999/delete",qs.stringify({hash:hash})).then((response) => {
            if (response.data != "error") {
              console.log(response.data)
                this.sites = response.data
                // Vue.delete(this.sites,hash)
                // this.handleshow();
            }
          }).catch((response) => {
            this.$Message.error({
              content: '查询出错！' + response,
            });
          })
        // this.sites = {"196d726763c95391e26a820bb787da7f":{"content":"\ud83d\udea8 NEW: CVE-2019-20880 \ud83d\udea8 An issue was discovered in Mattermost Server before 5.8.0, 5.7.2, 5.6.5, and 4.10.7. It allows attackers to cause a denial of service (memory consumption) via OpenGraph. Severity: HIGH https://t.co/ZFtLGVOKht","hash":"196d726763c95391e26a820bb787da7f","time":"Sat Jun 20 22:35:56 +0000 2020"},"1bdf16237ba1256291c788bafea92bbb":{"content":"@rushadthomas @SpacemanEd @notlarrysabato @AdamParkhomenko I don\u2019t know you or anything about this person or these accusations but I just wanted to stop my scrolling and tell you that this comment is lovely and I wish more people thought/felt/behaved the way you do.","hash":"1bdf16237ba1256291c788bafea92bbb","time":"Sun Jun 21 01:52:58 +0000 2020"}}

    },

    handleshow () {
      axios.get("http://127.0.0.1:9999/show").then((response) => {
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
