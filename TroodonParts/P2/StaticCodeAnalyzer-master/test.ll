; ModuleID = '/home/user-admin/Downloads/Data_Generation/Matrix_Mul/CPU/matrixmul_kernel.cl'
source_filename = "/home/user-admin/Downloads/Data_Generation/Matrix_Mul/CPU/matrixmul_kernel.cl"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: convergent nounwind uwtable
define spir_kernel void @matrixMul(float* nocapture, float* nocapture readonly, float* nocapture readonly, i32, i32) local_unnamed_addr #0 !kernel_arg_addr_space !3 !kernel_arg_access_qual !4 !kernel_arg_type !5 !kernel_arg_base_type !5 !kernel_arg_type_qual !6 {
  %6 = tail call i32 (i32, ...) bitcast (i32 ()* @get_global_id to i32 (i32, ...)*)(i32 0) #3
  %7 = tail call i32 (i32, ...) bitcast (i32 ()* @get_global_id to i32 (i32, ...)*)(i32 1) #3
  %8 = icmp sgt i32 %3, 0
  %9 = mul nsw i32 %7, %3
  br i1 %8, label %10, label %33

; <label>:10:                                     ; preds = %5
  %11 = sext i32 %4 to i64
  %12 = sext i32 %6 to i64
  %13 = sext i32 %9 to i64
  %14 = zext i32 %3 to i64
  %15 = and i64 %14, 1
  %16 = icmp eq i32 %3, 1
  br i1 %16, label %19, label %17

; <label>:17:                                     ; preds = %10
  %18 = sub nsw i64 %14, %15
  br label %38

; <label>:19:                                     ; preds = %38, %10
  %20 = phi float [ undef, %10 ], [ %58, %38 ]
  %21 = phi i64 [ 0, %10 ], [ %59, %38 ]
  %22 = phi float [ 0.000000e+00, %10 ], [ %58, %38 ]
  %23 = icmp eq i64 %15, 0
  br i1 %23, label %33, label %24

; <label>:24:                                     ; preds = %19
  %25 = add nsw i64 %21, %13
  %26 = getelementptr inbounds float, float* %1, i64 %25
  %27 = load float, float* %26, align 4, !tbaa !7
  %28 = mul nsw i64 %21, %11
  %29 = add nsw i64 %28, %12
  %30 = getelementptr inbounds float, float* %2, i64 %29
  %31 = load float, float* %30, align 4, !tbaa !7
  %32 = tail call float @llvm.fmuladd.f32(float %27, float %31, float %22)
  br label %33

; <label>:33:                                     ; preds = %24, %19, %5
  %34 = phi float [ 0.000000e+00, %5 ], [ %20, %19 ], [ %32, %24 ]
  %35 = add nsw i32 %9, %6
  %36 = sext i32 %35 to i64
  %37 = getelementptr inbounds float, float* %0, i64 %36
  store float %34, float* %37, align 4, !tbaa !7
  ret void

; <label>:38:                                     ; preds = %38, %17
  %39 = phi i64 [ 0, %17 ], [ %59, %38 ]
  %40 = phi float [ 0.000000e+00, %17 ], [ %58, %38 ]
  %41 = phi i64 [ %18, %17 ], [ %60, %38 ]
  %42 = add nsw i64 %39, %13
  %43 = getelementptr inbounds float, float* %1, i64 %42
  %44 = load float, float* %43, align 4, !tbaa !7
  %45 = mul nsw i64 %39, %11
  %46 = add nsw i64 %45, %12
  %47 = getelementptr inbounds float, float* %2, i64 %46
  %48 = load float, float* %47, align 4, !tbaa !7
  %49 = tail call float @llvm.fmuladd.f32(float %44, float %48, float %40)
  %50 = or i64 %39, 1
  %51 = add nsw i64 %50, %13
  %52 = getelementptr inbounds float, float* %1, i64 %51
  %53 = load float, float* %52, align 4, !tbaa !7
  %54 = mul nsw i64 %50, %11
  %55 = add nsw i64 %54, %12
  %56 = getelementptr inbounds float, float* %2, i64 %55
  %57 = load float, float* %56, align 4, !tbaa !7
  %58 = tail call float @llvm.fmuladd.f32(float %53, float %57, float %49)
  %59 = add nuw nsw i64 %39, 2
  %60 = add i64 %41, -2
  %61 = icmp eq i64 %60, 0
  br i1 %61, label %19, label %38
}

; Function Attrs: convergent
declare i32 @get_global_id() local_unnamed_addr #1

; Function Attrs: nounwind readnone speculatable
declare float @llvm.fmuladd.f32(float, float, float) #2

attributes #0 = { convergent nounwind uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { convergent "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #2 = { nounwind readnone speculatable }
attributes #3 = { convergent nounwind }

!llvm.module.flags = !{!0}
!opencl.ocl.version = !{!1}
!llvm.ident = !{!2}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 1, i32 0}
!2 = !{!"clang version 6.0.0-1ubuntu2 (tags/RELEASE_600/final)"}
!3 = !{i32 1, i32 1, i32 1, i32 0, i32 0}
!4 = !{!"none", !"none", !"none", !"none", !"none"}
!5 = !{!"float*", !"float*", !"float*", !"int", !"int"}
!6 = !{!"", !"", !"", !"", !""}
!7 = !{!8, !8, i64 0}
!8 = !{!"float", !9, i64 0}
!9 = !{!"omnipotent char", !10, i64 0}
!10 = !{!"Simple C/C++ TBAA"}
