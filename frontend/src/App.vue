<template>
  <div id="app">
    <el-container>
      <el-aside width="200px">
        <el-menu background-color="#545C64" text-color="#FFF" active-text-color="#FFD04B" router="true" style="height: 100%;">
          <el-submenu index="1">
            <template slot="title"><i class="el-icon-setting"></i><span>合同管理</span></template>
              <el-menu-item-group>
                <el-menu-item index="1-1">1-1</el-menu-item>
                <el-menu-item index="1-2">1-2</el-menu-item>
              </el-menu-item-group>
          </el-submenu>
          <el-submenu index="2">
            <template slot="title"><i class="el-icon-setting"></i><span>合同管理</span></template>
              <el-menu-item-group>
                <el-menu-item index="2-1">2-1</el-menu-item>
                <el-menu-item index="2-2">2-2</el-menu-item>
              </el-menu-item-group>
          </el-submenu>
          <el-submenu index="3">
            <template slot="title"><i class="el-icon-setting"></i><span>合同管理</span></template>
              <el-menu-item-group>
                <el-menu-item index="3-1">3-1</el-menu-item>
                <el-menu-item index="3-2">3-2</el-menu-item>
              </el-menu-item-group>
          </el-submenu>
        </el-menu>
      </el-aside>

      <el-container>
        <el-header height="56px" style="background-color: #545C64; text-color: #FFF;">
          <el-dropdown>
            <span>设置<i class="el-icon-arrow-down"></i></span>
          </el-dropdown>
        </el-header>
        <el-main>
          <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
html, body, #app, .el-container, .el-aside {
  height: 100%;
  margin: 0;
  font-family: Helvetica Neue,Helvetica,PingFang SC,Hiragino Sans GB,Microsoft YaHei,SimSun,sans-serif;
  font-weight: 400;
  -webkit-font-smoothing: antialiased;
}

</style>
