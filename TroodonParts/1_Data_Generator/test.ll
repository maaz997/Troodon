; ModuleID = '/home/user-admin/Desktop/2.0/Troodon/1_Data_Generator/matrixT_kernel.cl'
source_filename = "/home/user-admin/Desktop/2.0/Troodon/1_Data_Generator/matrixT_kernel.cl"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: convergent nounwind uwtable
define spir_kernel void @matrixMul(float* nocapture, float* nocapture readonly, float* nocapture readnone, i32, i32) local_unnamed_addr #0 !kernel_arg_addr_space !3 !kernel_arg_access_qual !4 !kernel_arg_type !5 !kernel_arg_base_type !5 !kernel_arg_type_qual !6 {
  %6 = tail call i32 (i32, ...) bitcast (i32 ()* @get_global_id to i32 (i32, ...)*)(i32 0) #2
  %7 = tail call i32 (i32, ...) bitcast (i32 ()* @get_global_id to i32 (i32, ...)*)(i32 1) #2
  %8 = mul nsw i32 %7, %3
  %9 = add nsw i32 %8, %6
  %10 = sext i32 %9 to i64
  %11 = mul nsw i32 %6, %3
  %12 = add nsw i32 %11, %7
  %13 = sext i32 %12 to i64
  %14 = getelementptr inbounds float, float* %1, i64 %13
  %15 = bitcast float* %14 to i32*
  %16 = load i32, i32* %15, align 4, !tbaa !7
  %17 = getelementptr inbounds float, float* %0, i64 %10
  %18 = bitcast float* %17 to i32*
  store i32 %16, i32* %18, align 4, !tbaa !7
  ret void
}

; Function Attrs: convergent
declare i32 @get_global_id() local_unnamed_addr #1

attributes #0 = { convergent nounwind uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { convergent "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #2 = { convergent nounwind }

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
