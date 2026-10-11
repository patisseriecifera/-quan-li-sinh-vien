import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# =========================
# CẤU HÌNH TRANG WEB APP
# =========================
st.set_page_config(
    page_title="Quản lý điểm sinh viên",
    page_icon="🎓",
    layout="wide"
)

st.title("QUẢN LÝ ĐIỂM SINH VIÊN")
st.write("Ứng dụng minh họa quản lý điểm, thống kê kết quả và tra cứu sinh viên.")

# =========================
# 1. TẠO DATAFRAME 10 SINH VIÊN
# =========================
data = {
    "Họ tên": [
        "Nguyễn Văn An",
        "Trần Thị Bình",
        "Lê Hoàng Nam",
        "Phạm Minh Anh",
        "Hoàng Quốc Bảo",
        "Võ Thị Lan",
        "Đặng Đức Huy",
        "Bùi Ngọc Mai",
        "Đỗ Thành Công",
        "Ngô Thùy Linh"
    ],
    "Chuyên cần": [9.0, 8.5, 7.5, 10.0, 8.0, 9.5, 7.0, 8.5, 6.5, 9.0],
    "Giữa kỳ":    [8.0, 7.5, 6.5, 9.0, 7.0, 8.5, 6.0, 8.0, 5.5, 9.0],
    "Cuối kỳ":    [8.5, 8.0, 7.0, 9.5, 7.5, 9.0, 6.5, 8.5, 6.0, 9.5]
}

df = pd.DataFrame(data)

# =========================
# 2. TÍNH ĐIỂM TỔNG KẾT
# Công thức: 20% chuyên cần + 30% giữa kỳ + 50% cuối kỳ
# =========================
df["Tổng kết"] = (
    0.2 * df["Chuyên cần"]
    + 0.3 * df["Giữa kỳ"]
    + 0.5 * df["Cuối kỳ"]
).round(2)

# =========================
# 3. XẾP LOẠI HỌC LỰC
# =========================
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7.0:
        return "Khá"
    elif diem >= 5.0:
        return "Trung bình"
    return "Yếu"

df["Xếp loại"] = df["Tổng kết"].apply(xep_loai)

# =========================
# 4. HIỂN THỊ BẢNG ĐIỂM
# =========================
st.subheader("1. Bảng điểm sinh viên")
st.dataframe(
    df[["Họ tên", "Chuyên cần", "Giữa kỳ", "Cuối kỳ", "Tổng kết", "Xếp loại"]],
    use_container_width=True,
    hide_index=True
)

# =========================
# 5. THỐNG KÊ TOÀN LỚP
# =========================
st.subheader("2. Thống kê kết quả học tập")

diem_trung_binh = df["Tổng kết"].mean()
diem_cao_nhat = df["Tổng kết"].max()
diem_thap_nhat = df["Tổng kết"].min()
so_sinh_vien_dat = int((df["Tổng kết"] >= 5).sum())
so_sinh_vien_chua_dat = int((df["Tổng kết"] < 5).sum())

sinh_vien_cao_nhat = df[df["Tổng kết"] == diem_cao_nhat]
sinh_vien_thap_nhat = df[df["Tổng kết"] == diem_thap_nhat]

m1, m2, m3, m4 = st.columns(4)
m1.metric("Điểm trung bình lớp", f"{diem_trung_binh:.2f}/10")
m2.metric("Điểm cao nhất", f"{diem_cao_nhat:.2f}")
m3.metric("Điểm thấp nhất", f"{diem_thap_nhat:.2f}")
m4.metric("Số sinh viên đạt (≥ 5)", f"{so_sinh_vien_dat}/{len(df)}")

st.write("**Sinh viên có điểm tổng kết cao nhất:**")
st.dataframe(
    sinh_vien_cao_nhat[["Họ tên", "Tổng kết", "Xếp loại"]],
    use_container_width=True,
    hide_index=True
)

st.write("**Sinh viên có điểm tổng kết thấp nhất:**")
st.dataframe(
    sinh_vien_thap_nhat[["Họ tên", "Tổng kết", "Xếp loại"]],
    use_container_width=True,
    hide_index=True
)

st.caption(f"Số sinh viên chưa đạt (điểm dưới 5): {so_sinh_vien_chua_dat}")

# =========================
# 6. TRA CỨU MỘT SINH VIÊN
# =========================
st.subheader("3. Tra cứu điểm theo sinh viên")
ten_duoc_chon = st.selectbox("Chọn một sinh viên:", df["Họ tên"].tolist())
sinh_vien = df[df["Họ tên"] == ten_duoc_chon].iloc[0]

st.markdown(f"**Thông tin điểm của sinh viên: {ten_duoc_chon}**")
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Chuyên cần", f'{sinh_vien["Chuyên cần"]:.1f}')
c2.metric("Giữa kỳ", f'{sinh_vien["Giữa kỳ"]:.1f}')
c3.metric("Cuối kỳ", f'{sinh_vien["Cuối kỳ"]:.1f}')
c4.metric("Tổng kết", f'{sinh_vien["Tổng kết"]:.2f}')
c5.metric("Xếp loại", sinh_vien["Xếp loại"])

# =========================
# 7. BIỂU ĐỒ CỘT
# =========================
st.subheader("4. Biểu đồ điểm tổng kết của 10 sinh viên")
fig, ax = plt.subplots(figsize=(12, 5))
bars = ax.bar(df["Họ tên"], df["Tổng kết"])
ax.set_title("Điểm tổng kết của 10 sinh viên")
ax.set_xlabel("Họ và tên sinh viên")
ax.set_ylabel("Điểm tổng kết (thang điểm 10)")
ax.set_ylim(0, 10)
ax.tick_params(axis="x", labelrotation=45)
for label in ax.get_xticklabels():
    label.set_horizontalalignment("right")
ax.bar_label(bars, fmt="%.2f", padding=3)
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

# =========================
# 8. THÔNG TIN NGƯỜI TẠO
# Thay thông tin mẫu bên dưới bằng họ tên và MSSV của bạn.
# =========================
st.divider()
st.markdown(
    """
    <div style="text-align: center; color: gray; font-size: 12px;">
        Người thực hiện: VŨ CƯỜNG THỊNH | MSSV: 031208008889
    </div>
    """,
    unsafe_allow_html=True
)
