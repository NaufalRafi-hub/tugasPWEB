<?php

$folderUpload = __DIR__ . "/assets/uploads";
$fileFoto = (object) @$_FILES['foto'];

if ($fileFoto->size > 1000 * 2000) {
    die("File tidak boleh lebih dari 2MB");}

if ($fileFoto->type !== 'image/jpeg') {
    die("File ktp harus jpeg!");}
# periksa apakah folder sudah ada
if (!is_dir($folderUpload))
{
# jika tidak maka folder harus dibuat terlebih dahulu
mkdir($folderUpload, 0777, $rekursif = true);
# simpan masing-masing file ke dalam array
# dan casting menjadi objek :)
};

# mulai upload file
$uploadFotoSukses = move_uploaded_file(
    $fileFoto->tmp_name, "{$folderUpload}/{$fileFoto->name}"
);

if ($uploadFotoSukses) {
    $link = "{$folderUpload}/{$fileFoto->name}";
    echo "Sukses Upload Foto: <a href='{$link}'>{$fileFoto->name}</a>";
    echo "<br>";
};


