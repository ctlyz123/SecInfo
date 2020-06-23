<template>
  <el-tabs v-model="activeName" @tab-click="handleClick">
    <el-tab-pane label="Unread" name="first" ><child1 v-if="isChildUpdate1"></child1></el-tab-pane>
    <el-tab-pane label="Mark" name="second" ><child2 v-if="isChildUpdate2"></child2></el-tab-pane>
<!--    <el-tab-pane label="角色管理" name="third">角色管理</el-tab-pane>-->
<!--    <el-tab-pane label="定时任务补偿" name="fourth">定时任务补偿</el-tab-pane>-->
  </el-tabs>
</template>


<script>
  import Unread from "./Unread";
  import Mark from "./Mark";
  export default {
      name: "TabView",
      components: {
          child1:Unread,
          child2:Mark
      },
    data() {
        return {
            //默认第一个选项卡
            activeName: "first",
            isChildUpdate1:true,
            isChildUpdate2:false
        }
    },
    methods:{
        handleClick(tab) {
            if(tab.name == "first") {
                this.isChildUpdate1 = true;
                this.isChildUpdate2 = false;
            } else if(tab.name == "second") {
                this.isChildUpdate1 = false;
                this.isChildUpdate2 = true;
            }
        }
    }
  };
</script>
